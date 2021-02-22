from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('all', views.get_all),
    path('pending', views.get_pending),
    path('update/<int:schedule_id>/<int:status_enum>', views.update)

]
