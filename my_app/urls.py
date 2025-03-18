from django.contrib import admin
from django.urls import path, include
from .views import my_list
urlpatterns = [
    path('', my_list, name="my_list"),
]



