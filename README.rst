==============
Flask QR
==============

This is simple extension for generating and displaying QR codes with flask.

.. _flask: http://flask.pocoo.org

Installation
------------

Install the extension with one of the following commands:
::

    $ easy_install Flask-QR

or alternatively if you have pip installed:
::

    $ pip install Flask-QR

How to Use
----------

Initialize with flask application and default parameters:
::

    qr = QR(app,
            mode="google",
            location="/qr/",
            errorCorrect='M',
            margin=4
            )

Then in your template:
::

    {{ 'I am a Qr-Code' | qrFor }}

Bigger and adult:
::

    {{ 'I am another bigger qrcode' | qrFor(400) }}

Parameters
~~~~~~~~~~

All parameters are described in the documentation...(TODO: Link when documentations are up)
