#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:00:36 2020

@author: cengqiqi
"""

import werobot
from werobot import WeRoBot
from werobot.replies import ArticlesReply, Article,ImageReply,TextReply

from weNewsModel.sender_wechatSender import get_title_text


robot = WeRoBot(enable_session=False,
                token='qiqi123',
                APP_ID='wx20e742b0ab9bfb54',
                APP_SECRET='be5e8743181098d92ac82bd80b758d57')

@robot.text
def echo(message):
    title, text = get_title_text()
    reply = TextReply(message=message, content=text)
    return reply

# 让服务器监听在 0.0.0.0:80
# robot.config['HOST'] = '0.0.0.0'
# robot.config['PORT'] = 443
# ß
