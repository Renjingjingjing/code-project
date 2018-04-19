#encoding: utf-8
__author__ = 'xwchen2'

from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from login.models import User, Goods

def index(req):
    users = User.objects.all()
    goods = Goods.objects.all()
    return render_to_response('index.html', locals(), context_instance=RequestContext(req))

