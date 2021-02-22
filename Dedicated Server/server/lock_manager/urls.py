from django.contrib import admin
from django.urls import path, include
from . import views

"""

Module: Lock Manager
Description: THe Lock Manager module is in charge of controlling access to the physical hardware device. 

The api below takes a parameter of num_id which is the id of the hardware device found in the dedicate's servers database
and another integer paramater of otp_pass, which is generated every 30 seconds, and requies a shared secret to generate. 

The API responds in json. With Either True or False, followed by a longer message if there were any errors.


api :     path('<int:num_id>/<int:otp_pass>/<int:tx_id>', views.verify),
Purpose : used by the port master to unlock the water staion
parameters : takes the id of the water station, takes a one time password associated with the id, takes a transaction_id



api : path('<int:num_id>/>', views.verify),
Purpose : used by the phyical hardware device to lock/unlock
parameters : takes the id of the water station. Returns string "locked"/"unlocked"



"""



urlpatterns = [
    path('<int:num_id>/<int:otp_pass>', views.access),
    path('status/<int:num_id>', views.status)
]
