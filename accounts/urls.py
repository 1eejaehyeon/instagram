from django.urls import path, re_path
from django.views.generic import TemplateView

from accounts import views

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path("edit/", views.profile_edit, name="edit"),
    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page'),
    re_path(r'^(?P<username>[\w.@+-]+)/follow/$', views.user_follow, name='user_follow'),
    re_path(r'^(?P<username>[\w.@+-]+)/user_unfollow/$', views.user_unfollow, name='user_unfollow'),

]