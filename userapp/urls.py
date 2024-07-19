from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
   
    path('',views.home,name='home'),
    path('base/',views.base,name='base'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('signup/',views.signup,name='signup'),
]