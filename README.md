# python-ueditor
python-django-ueditor


在VUE中结合ueditor 使用django进行文件上传

vue中使用ueditor参考
https://www.cnblogs.com/dmcl/p/7152711.html



api.py  处理文件上传以及编辑器对配置进行请求 

image_upload

ueditor加载配置的时候每次会去服务器请求配置 

action为config 从服务器返回配置

为uploadimage 上传图片 对图片进行处理



config.json 配置文件
详细设置参考：http://fex.baidu.com/ueditor/#server-deploy



django 创建API文件夹 放入api.py 名字随意
创建一个URL 指向api文件image_upload
更改\static\UE\ueditor.config.js
serverUrl: django指向api文件image_upload 方法的路由

