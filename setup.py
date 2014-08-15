"""
Flask-QR
-------------
"""
from setuptools import setup


setup(
    name='Flask-QR',
    version='0.1.1',
    url='https://github.com/danielwarna/Flask-QR/',
    license='BSD',
    author='Daniel Warna',
    author_email='daniel@danielwarna.com',
    description='Flask extension for generating qr codes',
    long_description=open('README.rst').read(),
    py_modules=['flask_qr'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'qrcode',
        'pillow'
    ],

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)