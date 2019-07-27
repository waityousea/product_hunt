from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'sign_up.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        password1 = request.POST['密码']
        password2 = request.POST['确认密码']
        try:
            User.objects.get(username = user_name)
            return render(request, 'sign_up.html',{'用户名错误':"该用户名已存在"})
        except User.DoesNotExist:
            if password1 == password2:
                User.objects.create_user(username=user_name, password= password1)
                return redirect('主页')
            else:
                return render(request, 'sign_up.html', {'密码错误': "两次输入的密码不一致"})

