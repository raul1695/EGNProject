from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('access/<int:num_id>/<int:otp_pass>', views.verify)
]
