from flask import current_app, url_for, Markup

import os.path
import urllib

import qrcode

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class QR(object):

    googleurl = "https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=http://www.lifehacker.com"

    errorCodes = {
        "L":qrcode.constants.ERROR_CORRECT_L,
        "M":qrcode.constants.ERROR_CORRECT_M,
        "Q":qrcode.constants.ERROR_CORRECT_Q,
        "H":qrcode.constants.ERROR_CORRECT_H
    }

    def __init__(self, app=None, mode="google", location="/qr/", errorCorrect="M", margin=4):
        self.app = app
        if app is not None:
            self.init_app(app, mode, location,errorCorrect, margin)

    def init_app(self, app, mode, location,errorCorrect, margin):
        app.config.setdefault('QRCODE_LOCATION', app.static_folder)

        if mode == "google":
            self.mode = mode
            import qrcode
        else:
            self.mode = "local"

        app.jinja_env.filters.setdefault('qr_for', self.qrForJinja)
        #app.jinja_env.globals.update(qr_for=self.qrFor)

        app.extensions['qr'] = self
        app.qr_folder = app.static_folder + location

        app.qr_path = app.static_url_path + location

        self.errorLevel = errorCorrect
        self.margin = margin

        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def qrForJinja(self, url, dimension=200):
        qrUrl = self.qrFor(url, dimension)

        #return url/for the image.
        return Markup("<img src="+qrUrl+" height=" + str(dimension) + " width="+ str(dimension) + ">")

    # Function called from jinja
    def qrFor(self, url, dimension=200):
        #Generate/get qr
        qr = ""
        if(self.mode == "google"):
            print "Generating google qr code " + url
            qr = self._googleQR(url, dimension)
        elif(self.mode == "local"):
            qr = self._localQR(url, dimension)
        
        return qr


    def _googleQR(self, url, dimension):
        if dimension > 540:
            dimension = 540

        base = "https://chart.googleapis.com/chart?"
        dimension = "chs=" + str(dimension)+ "x" + str(dimension)
        qr = "cht=qr&chl=" + urllib.quote_plus(url)
        error = "chld=" + self.errorLevel
        return base + dimension + "&" +  qr + "&" + error +"|" + str(self.margin)
        

    def _localQR(self, url, dimension):
        url = url.replace("https://", "").replace("http://", "")
        fileName = urllib.quote_plus(url) + str(dimension) + str(self.margin) +".png"
        filePath = os.path.join(self.app.qr_folder, fileName)
        if (os.path.isfile(filePath)):
            print "qr exists, returning url"
            pass
        else:
            #filePath = os.path.join(self.app.qr_folder, fileName)
            f = open(filePath, "w")
            #Generate qr and write it to file.
            qr = qrcode.make(url, error_correction=self.errorCodes[self.errorLevel], border=self.margin)
            #qr._img = qr._img.resize(300, 150,resize_canvas=True)1
            qr.save(f)
            f.close()


        return self.app.qr_path + fileName


    def teardown(self, exception):
        print "Trearing down"
