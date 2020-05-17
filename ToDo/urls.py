from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^tasks/(?P<id>[0-9]{1,})/$',views.todo_list, name='homepage'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.loginuser, name='login'),
    re_path(r'^tasks/(?P<id>[0-9]{1,})/new/$',views.add_task,name='newtask'),
    re_path(r'^tasks/(?P<user_id>[0-9]{1,})/(?P<task_id>[0-9]{1,})/update/$',views.update_task,name='updatetask'),
    re_path(r'^tasks/(?P<user_id>[0-9]{1,})/(?P<task_id>[0-9]{1,})/delete/$',views.delete_task,name='deletetask'),
    path('logout/', views.logout_view, name='logout'),
    #path('login/user/signup',views.signup,name='signup')
    #re_path(r'^login/user/*$',views.loginuser,name='login'),
    #path('login/signup',views.signup, name='signup'),
]