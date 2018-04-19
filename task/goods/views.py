#encoding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
import controller
from django.template import RequestContext
import task.function as fun
from django import forms


class FileForm(forms.Form):
    id = forms.IntegerField(required=False)
    fileform = forms.FileField()


def default(req):
    if not req.session['islogin']:
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    ui = req.session['user_info']['id']
    print ui
    goods_info = controller.get_goods_info(ui)
    uf = FileForm()
    return render_to_response('goods.html', locals(), context_instance=RequestContext(req))


def post(req):
    if not req.session['islogin']:
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    if req.method != "POST":
        return HttpResponse('unsupport method!')
    data = fun.warp_data(req.POST)
    ui = req.session['user_info']['id']
    data['ui'] = ui
    rt = controller.goods_post(data)
    print rt
    if rt:
        return HttpResponseRedirect('/goods/default')
    else:
        msg = '提交物品信息失败,请联系管理员！'
        return render_to_response('msg.html', locals())


def picture(req, id):
    print req
    # print id
    goods_info = controller.get_goods_one(id)
    uf = FileForm()
    return render_to_response('picture.html', locals(), context_instance=RequestContext(req))


def upload(req):
    id = req.POST['id']
    goods_info = controller.get_goods_one(id)
    f = req.FILES.get('picture', None)
    print f
    print type(f)
    if fun.picture_uploaded(f):
        goods_info.picture = f.name
        # print goods_info.picture
        goods_info.save()
        return HttpResponseRedirect('/goods/default')
    else:
        return HttpResponse('upload fail!')


def preview(req):
    if not req.session['islogin']:
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    goods_info = controller.get_goods_info(uid)
    # if goods_info:
    #     goods_id = goods_info.id
    # else:
    #     goods_info = {}
    uf = FileForm()
    return render_to_response('view.html', locals(), context_instance=RequestContext(req))


def search(req):
    data = fun.warp_data(req.POST)
    keywords = data.get('keywords')
    # print keywords
    goods_list = controller.goods_search(keywords)
    for i in goods_list:
        print i.is_available
        if i.is_available == 1:
            i.is_available = '失效'
        elif i.is_available == 0:
            i.is_available = '正常'
    return render_to_response('goods_search.html', locals(), context_instance=RequestContext(req))
