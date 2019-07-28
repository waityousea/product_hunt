from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


# Create your views here.


def product_list(request):
    return render(request,'product_list.html')


@login_required
def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    elif request.method == 'POST':
        title = request.POST['标题']
        intro = request.POST['介绍']
        url = request.POST['APP链接']
        #icon = request.FILES['APP图标']

        try:
            icon = request.FILES['APP图标']
            image = request.FILES.get('大图')

            product = Product()
            product.title = title
            product.intro = intro
            product.url = url
            product.icon = icon
            product.image = image
            # 发布日期
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user

            product.save()
            return redirect('主页')

        except Exception as err:
            return render(request, 'publish.html',{'错误':'请上传图片!'})




