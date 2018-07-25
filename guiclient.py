# -*- coding: utf8 -*-

import Tkinter as tk
import tkFont as tkf
import requests

LP_HOST = 'localhost'
LP_PORT = 51023
LP_URI = 'http://%s:%s/p' % (LP_HOST, LP_PORT)

def on_click():
    # get content from text editor
    ctt = text.get('0.0', tk.END)
    label['text'] = 'Sending content (%s)...' % len(ctt)
    
    # send the content 
    data = {'c':ctt, 'r':'json'}
    rsp = requests.post(LP_URI, data=data)
    
    # update GUI
    label['text'] = 'Sent! Return %s. Print more?' % rsp.status_code

    
root = tk.Tk(className='* Note POS Client *')
root.resizable(False, False)

label = tk.Label(root)
label['text'] = 'Write Notes and Print it!'
label.pack(fill='x', pady=5)

frm_main = tk.Frame(height=100)
frm_main.pack(pady=5)
scrollbar = tk.Scrollbar(frm_main)
scrollbar.pack(side='right', fill='y')

text = tk.Text(frm_main, yscrollcommand=scrollbar.set, \
    width=30, height=10, font=tkf.Font(size=16))
scrollbar.config(command=text.yview)
text.pack(side='left')

btn_send = tk.Button(root)
btn_send['text'] = 'PRINT ABOVE CONTENT !'
btn_send['command'] = on_click
btn_send.pack(fill='x', pady=5)

root.mainloop()
