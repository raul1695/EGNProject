from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt


"""


The transmit



"""

urlpatterns = [
    path('transmit/', csrf_exempt(views.send_req))
]
