from django.urls import path, include

from credentials import views
from django.conf.urls.static import static

urlpatterns = [

    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
    ]