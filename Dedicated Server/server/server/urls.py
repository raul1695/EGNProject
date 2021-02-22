"""server URL Configuration
server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


"""



LOCK_MANAGER : Handles the locking/unlocking of the water station hardware

PORT_MANAGER : Handles syncronizity of all water station usage (e.i: when a tablet scans a qr code it provides certain information to user)

REQUEST_MANAGER : Handles the Image-related detection. Allows users to recieve images and upload data.



"""
from django.urls import path, include

urlpatterns = [
    path('access/', include('lock_manager.urls')),
    path('request/', include('request_manager.urls')),
    path('schedule/', include('schedule_manager.urls')),
    path('tx/', include('transaction_manager.urls'))
]