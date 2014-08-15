Flask-QR
========

This is simple extension for generating and displaying QR codes with flask_.


Installation
------------

Install the extension with one of the following commands:

.. code-block:: sh

    $ pip install Flask-QR

or alternatively if you have pip installed:

.. code-block:: sh

    $ easy_install Flask-QR
    

Quickstart
----------

Initialize with flask application and default parameters:

.. code-block:: python

    from flask_qr import QR

    qr = QR(app, mode="google")

Then in your template:

.. code-block:: python

    {{ 'I am a Qr-Code' | qrFor }}


Api
---

.. class:: flask_qr.QR(app=None, mode="google", location="/qr/", errorCorrect="M", margin=4)
    
    Object for creating qr codes and links to them.

    .. method:: qrFor(url, dimension=200):

        Generates a qr code and returns the url.

        :param message: data to encode in the qr code.
        :param dimension: size of the qr code.

    .. method:: qrForJinja(message, dimension=200):

        Embedds the qr code in an html image tag.

        :param message: data to encode in the qr code.
        :param dimension: size of the qr code.


Options
-------

+-----------------------+-------------------------------------------------------+
| Option Name           | Description                                           |
+=======================+=======================================================+
| ``mode``              | Select which mode to use, either 'local' or 'google'  |
+-----------------------+-------------------------------------------------------+
| ``margin``            | Set the margin width. Not that the width is given in  |
|                       | number of qr code rows_.                              |
+-----------------------+-------------------------------------------------------+ 
| ``errorCorrect``      | Set the `error correction`_ level of the qr code.     |
|                       |                                                       |
|                       | * L - Allows recovery of up to 7% data loss           |
|                       | * M - [Default] Allows recovery of up to 15% data loss|
|                       | * Q - Allows recovery of up to 25% data loss          |
|                       | * H - Allows recovery of up to 30% data loss.         | 
|                       |                                                       | 
+-----------------------+-------------------------------------------------------+ 
| ``location``          | When using local mode, specify where in the static    |
|                       | folder qr codes should be stored                      |
+-----------------------+-------------------------------------------------------+ 


.. _flask: http://flask.pocoo.org/
.. _qrcode: https://pypi.python.org/pypi/qrcode/
.. _pillow: https://pypi.python.org/pypi/Pillow
.. _rows: https://developers.google.com/chart/infographics/docs/qr_codes#details
.. _`graph api`: https://developers.google.com/chart/infographics/docs/qr_codes#details
.. _`error correction`: https://developers.google.com/chart/infographics/docs/qr_codes#details

