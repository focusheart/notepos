# Note POS

## Introduction

A program for thermal printer on Raspberry Pi 
(I have tested on RPi models `1 B`, `2 B+` , `3 B` . Maybe other Linux systems work too).
I wrapped the printer(/dev/usb/lp0) and provided interface on HTTP.
Meanwhile, a GUI and a web page were provided for using interface.
Have fun!

## Requirements

There are several dependency packages:

* flask
* gunicorn(optional, but recommended)
* requests (optional)
* Tkinter (optional)
* tkFont (optional)

And, a USB thermal printer (supporting ESC/POS is better).
I bought a cheap one on Taobao at about $13, which is good enough.
The optional packages were used in the GUI client,
which means you can ignore these optional packages if you use web page only.

Installing dependency packages is quite easy on RPi:

    $ sudo apt-get install python-flask gunicorn
    
Other packages can also be installed by `apt-get`.

## Usage

Switch to root user (this is required for accessing thermal printer),
you can change the `LP_HOST` & `LP_PORT` in `server.py` according to your case.
The default values, `192.168.1.102` and `51023`, were used in my place.

Most importantly, you MUST check the printer's path:

    $ ls /dev/usb/
    
If the `lp0` exists, you can start the server now.
Otherwise, if `lp1` or other number exists, 
which means your thermal printer location is different than default,
you should change the `LP_PATH` in `server.py` as it is in `/dev/usb/`.

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
