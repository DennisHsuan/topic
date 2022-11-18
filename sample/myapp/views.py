from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import productModel

def index(request):
    # ORM"取"全部資料是用.all 單筆則是.get 
    #    "放"資料是用append
    products=productModel.objects.all()#取產品資料
    productlist=[]#因為只要取資料夾裡面8張照片
    for i in range(1, 9):
        product = productModel.objects.get(id = i)
        productlist.append(product)
    # print(products) #取得成功測試


    # return HttpResponse("你好")
    return render(request, 'index.html', locals())
