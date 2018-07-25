#!/bin/sh

echo '* starting gunicorn ...'
gunicorn -D -w 1 --pid notepos.pid -b 0.0.0.0:51023 server:app

echo '* done, have a look on the process:' 
ps aux | grep server
