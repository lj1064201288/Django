from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from pymysql import connect
from .models import DaiLi
from django.template.loader import get_template


def daili(request):
    return HttpResponse('西刺代理')

def index(request):
    template = get_template('xici.html')
    highs = DaiLi.objects.filter(isanonymous='高匿')[:20]
    lucencys = DaiLi.objects.filter(isanonymous='透明')[:20]
    https_list = DaiLi.objects.filter(type='https')[:20]
    http_list = DaiLi.objects.filter(type='http')[:20]
    socket_list = DaiLi.objects.filter(type='socks4/5')[:20]

    html = template.render(locals())

    return HttpResponse(html)





