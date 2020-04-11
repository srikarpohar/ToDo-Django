from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.loginuser, name='login'),
    #path('login/user/signup',views.signup,name='signup')
    #re_path(r'^login/user/*$',views.loginuser,name='login'),
    #path('login/signup',views.signup, name='signup'),
]