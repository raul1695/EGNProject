from django.shortcuts import render
from django.http import JsonResponse
from . import core
# Create your views here.


def get_all(request):
	data = core.get_all_schedules()
	return JsonResponse(data, safe = False)

def update(request, schedule_id,status_enum):
	data = {'response' : core.update_status(schedule_id,status_enum)}
	return JsonResponse(data)

def get_pending(request):
	data = core.get_pending()
	return JsonResponse(data, safe = False)