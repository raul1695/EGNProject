
from django.shortcuts import render
from django.http import JsonResponse
from . import core



"""
Views for the api of lock_manager

"""
def access(request, num_id,otp_pass):

	answer = core.change_lock_state(num_id, otp_pass)

	data = {'openLock' : answer,
			'otp password attempted (Debugging purposes)': otp_pass
			}
	
	return JsonResponse(data)


def status(request, num_id):

	answer = core.check_status(num_id)

	data = {'Lock_status' : answer
			}
	
	return JsonResponse(data)


def all(request):
	data = core.get_all_lock()
	return JsonResponse(data, safe = False)
