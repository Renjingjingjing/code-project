#encoding: utf-8
__author__ = 'renjing'

from login.models import Goods
from task import function as fun


def get_goods_info(ui):
    try:
        return Goods.objects.filter(ui=ui)
    except:
        return []


def get_goods_one(id):
    print id
    try:
        return Goods.objects.get(id=id)
    except:
        return []


def goods_post(data):
    id = data.pop('id')
    data['create_date'] = fun.now()
    data['is_available'] = 0
    print data
    if id:  # 更新
        return Goods.objects.filter(id=id).update(**data)
    else:   # 插入
        r = Goods(**data)
        r.save()
        return r


def goods_search(keywords):
    qs = Goods.objects.filter(goods=keywords)
    return qs