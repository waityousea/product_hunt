
from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/',views.sign_up, name='注册页面' ),
    path('login/',views.login, name='登录页面' ),
    path('logout/',views.logout, name='退出页面' ),
]