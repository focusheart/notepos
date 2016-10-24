# Note POS

## Introduction

A program for thermal printer on Raspberry Pi (and maybe other Linux systems).
I wrapped the printer(/dev/usb/lp0) and provided interface on HTTP.
Meanwhile, a GUI and a web page were provided for using interface.
Have fun!

## Requirements

There are several dependency packages:

* flask
* requests
* Tkinter
* tkFont
* gunicorn(optional)

And, a USB thermal printer (supporting ESC/POS is better).
I bought a cheap one on Taobao at about $13, which is good enough.

## Usage

Switch to root user (this is required for accessing thermal printer),
you can change the `LP_HOST` & `LP_PORT` in `server.py` according to your case.
The default values, `192.168.1.102` and `51023`, were used in my place.

Start this program using flask internal webserver Werkzeug:
    
    $ sudo su
    # python server.py

Or using gunicorn:

    # gunicorn -D -w 1 -b 0.0.0.0:51023 server:app

I have already wrapper this command in `run.sh`:

    # ./run.sh

Once the server is started, open a browser on your desktop or cell phone,
goto http://192.168.1.102:51023/, write some and press PRINT button.

Or, you can run the following command to open a GUI on your desktop,
I have tested on Windows, MacOS and Ubuntu and it works on all of them.
It is ugly, but works. I will try to make it better looking.

    $ python guiclient.py

Write something and press the PRINT button.
