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

