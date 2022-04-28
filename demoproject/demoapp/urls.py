from django.contrib import admin
from django.urls import path, include

from demoapp import views
from django.conf.urls.static import static

urlpatterns = [

    path('', views.demo, name='demo'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
#     path('detail/', views.detail, name='detail'),
#     path('thanks/', views.thanks, name='thanks'),
#
#     path('opr/', views.operation, name='operation'),
#     path('sub/', views.sub, name='sub'),
#
#     path('mul/', views.mul, name='mul'),
#
#     path('div/', views.div, name='div'),
]