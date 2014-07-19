========
Flask-QR
========

This is simple extension for generating and displaying QR codes with 'flask'_.

.. _flask: http://flask.pocoo.org

Installation
------------

Install the extension with one of the following commands:
::

    $ easy_install Flask-QR

or alternatively if you have pip installed:
::

    $ pip install Flask-QR

Quickstart
----------

Initialize with flask application and default parameters:
::

    qr = QR(app, mode="google")

Then in your template:
::

    {{ 'I am a Qr-Code' | qrFor }}


Documentation
~~~~~~~~~~~~~

The full documentation is available here. (TODO, link to docs)
