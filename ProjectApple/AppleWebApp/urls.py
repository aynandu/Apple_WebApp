from django.contrib import admin
from django.urls import path,include
from AppleWebApp import views


app_name='AppleWebApp'

urlpatterns = [
    path('',views.allProducts,name='allProducts'),
]