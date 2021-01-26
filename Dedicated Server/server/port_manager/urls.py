from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<berth_id>/<int:access_key>', views.lookup)
    
]
