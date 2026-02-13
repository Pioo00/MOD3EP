from django.apps import AppConfig
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

class MyinventoryappConfig(AppConfig):
    name = 'MyInventoryApp'
