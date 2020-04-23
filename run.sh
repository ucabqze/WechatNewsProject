#!/bin/bash

nohup gunicorn -w 2 WechatNewsProject.wsgi -b 0.0.0.0:80 > /tmp/gunicon.log 2>&1 &
