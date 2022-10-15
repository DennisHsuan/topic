from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import productModel

def index(request):
    products=productModel.objects.all()#取產品資料
    print(products) #取得成功測試


    # return HttpResponse("你好")
    return render(request, 'index.html', locals())
