from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:num_id>/<int:otp_pass>', views.verify)
]
