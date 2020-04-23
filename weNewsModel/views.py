from django.shortcuts import render
from django.http import HttpResponse
from weNewsModel.sender_newsSearhcer import open_current_file
from weNewsModel.sender_wechatSender import get_title_text

# Create your views here.
def print_text(request):
    return HttpResponse('Hello World')

def send_news(request):
    title, text = get_title_text()
    return HttpResponse(text)



import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from wechatpy import parse_message, create_reply


#django默认开启csrf防护，这里使用@csrf_exempt去掉防护
@csrf_exempt
def weixin_main(request):
    if request.method == "GET":
        #接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        #服务器配置中的token
        token = 'qiqi123'
        #把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist]).encode('utf-8')
        hashstr = hashlib.sha1(hashstr).hexdigest()
        if hashstr == signature:
          return HttpResponse(echostr)
        else:
          return HttpResponse("error")
    else:
        # othercontent = autoreply(request)
        # return HttpResponse(othercontent)
        msg = parse_message(request.body)
        if msg.type == 'text':
            title, text = get_title_text()
            print(text)
            reply = create_reply(text, msg)
        elif msg.type == 'image':
            reply = create_reply('这是条图片消息', msg)
        elif msg.type == 'voice':
            reply = create_reply('这是条语音消息', msg)
        else:
            reply = create_reply('这是条其他类型消息', msg)
        response = HttpResponse(reply.render(), content_type="application/xml")
        return response
    
    
    
    