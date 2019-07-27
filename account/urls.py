
from django.urls import path
from . import views

urlpatterns = [
    path('sign_up',views.sign_up, name='注册页面' ),

]