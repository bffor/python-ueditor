from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

import os
import uuid
import json
import datetime as dt
import re


# 目录创建
def upload_generation_dir(dir_name):
    today = dt.datetime.today()
    filedir='/%d/%d/' % (today.year, today.month)
    url_part = dir_name + filedir
    if not os.path.exists(url_part):
        os.makedirs(url_part)
    return url_part,filedir


# 图片上传
@csrf_exempt
def image_upload(request):
    if request.GET.get('action') == 'config':
        f = open('config.json',encoding = 'utf-8')
        data=f.read()
        f.close()
        temp=json.loads(data)
        callbackname=request.GET.get('callback')
        #防止XSS 过滤  callbackname只需要字母数字下划线
        pattern = re.compile('\w+',re.U)
        matchObj=re.findall(pattern, callbackname, flags=0)
        callbacks=matchObj[0]+'('+json.dumps(temp)+')'
        return HttpResponse(callbacks)
        
    elif request.GET.get('action') == 'uploadimage':
        img=request.FILES.get('upfile')
        name=request.FILES.get('upfile').name

        allow_suffix = ['jpg', 'png', 'jpeg', 'gif', 'bmp']
        file_suffix = name.split(".")[-1]
        
        if file_suffix not in allow_suffix:
            return {"state":'error',"name":name,"url":"","size":"","type":file_suffix}
        #上传文件路径
        dir_name='F:/stu/py-stu/firstpro/manage-system/static/img/'
        url_part,filedir= upload_generation_dir(dir_name)
        
        file_name = str(uuid.uuid1()) + "." + file_suffix
        path_file = os.path.join(url_part, file_name)
        file_url =url_part +file_name
        filenameurl='/static/img/'+filedir+file_name
        with open(file_url, 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        data= {"state":'SUCCESS',"url":filenameurl,"title":file_name,"original":name,"type":file_suffix,'size':'111'}
        return HttpResponse(json.dumps(data))
        
        
        