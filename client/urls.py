from django.urls import  path
from .import views
from django.contrib import admin

urlpatterns = [
    path('/<str:pk>/',views.List_client,name='client'),
]