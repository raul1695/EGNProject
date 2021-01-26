from django.shortcuts import render
from django.http import JsonResponse
from . import core
# Create your views here.


def lookup(request, berth_id,access_key):

	if(otp_pass == 1):
		answer = core.verify(num_id, otp_pass)
		data = {'openLock' : answer,
			'otp password attempted': otp_pass,
			'correct_password': core.generate_otp("UJFUW2N2GEJF4AIN")
			}
	
	return JsonResponse(data)
