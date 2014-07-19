from flask import Flask, url_for, render_template

from flask_qr import QR

app = Flask(__name__)

app.config['DEBUG'] = True
app.config.from_object('config') 

#qr = QR(app, mode="local")
qr = QR(app, mode="local",errorCorrect="Q")

@app.route("/")
def index():
    q = qr.qrFor("This_is_a_testqrcode")
    print q
    return render_template("base.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0')