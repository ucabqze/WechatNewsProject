#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:43:35 2020

@author: cengqiqi
"""

import requests

import weNewsModel.sender_config as cfg
import weNewsModel.sender_newsSearhcer as ns

import argparse
import datetime

###############################################################################

def get_title_text():
    
    # 设定参数
    news_num = 5
    save_dir =  cfg.save_dir
    start_date, end_date = auto_date_range()
    # start_date = '2020-04-15'
    # end_date = '2020-04-20'
    keyword_dict = {'的': 0.8}
    
    # 找到相关文章的路径
    related = ns.get_related_news(save_dir, start_date, end_date, keyword_dict)
    top_path_list = ns.top_news(related, news_num)
    
    # 获取文章标题\文章链接
    url_list = []
    title_list = []
    news_date_list= []
    for path in top_path_list: 
        url, title, news_date, text = ns.open_current_file(path)
        url_list.append(url)
        title_list.append(title)
        news_date_list.append(news_date)
        
        
    # 微信推送
    
    title = "对公业务组新闻推送"
    
    text = ('你好，以下是过去一周的新闻推送内容：\n\n'
            '{date0} - {title0}: {url0} \n\n '
            '{date1} - {title1}: {url1} \n\n '
            '{date2} - {title2}: {url2} \n\n '
            '{date3} - {title3}: {url3} \n\n '
            '{date4} - {title4}: {url4} \n\n').format(
            date0 = news_date_list[0], title0 = title_list[0], url0 = url_list[0],
            date1 = news_date_list[1], title1 = title_list[1], url1 = url_list[1],
            date2 = news_date_list[2], title2 = title_list[2], url2 = url_list[2],
            date3 = news_date_list[3], title3 = title_list[3], url3 = url_list[3],
            date4 = news_date_list[4], title4 = title_list[4], url4 = url_list[4],
            )
    
                
    return title, text


def auto_date_range():
    
    """ 获取过去一周的起始时间"""
    
    end = datetime.date.today()
    start = end - datetime.timedelta(days=7)
    
    start = start.strftime("%Y-%m-%d")
    end = end.strftime("%Y-%m-%d")
    
    return start, end


