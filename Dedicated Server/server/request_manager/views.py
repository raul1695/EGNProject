from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def send_req(request):
	if(request.method == 'POST'):
		body_unicode = request.body.decode('utf-8')
		person= {'firstname': 'Craig', 'lastname': 'Daniels'}
		json1111 = {'body_response' : body_unicode}
		context = {
        'person': person,
        'json1111': json1111,
        }
		return render(request, "request_manager/request.html", context)
	else:
		person= {'firstname': 'Failed', 'lastname': 'Attempt'}
		json1111 = "failed"
		context = {
        'person': person,
        'json1111': json1111,
        }
		return render(request, "request_manager/request.html", context)

"""
	if request.method == 'POST':
		return render(request,access_key)
	else:
		return render(request,access_key)
"""