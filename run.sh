#!/bin/sh

gunicorn -D -w 1 --pid notepos.pid -b 0.0.0.0:51023 server:app

ps aux | grep server
