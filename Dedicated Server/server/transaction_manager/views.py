from django.shortcuts import render
from django.http import JsonResponse
from . import core
import json
from types import SimpleNamespace
from django.views.decorators.csrf import csrf_exempt
import base64
from PIL import Image
import io

# Create your views here.


def get_all_tx(request):
	data = core.get_all_tx()
	return JsonResponse(data, safe = False)

@csrf_exempt
def generate_tx(request):
	if(request.method == 'POST'):
		try:
			body_unicode = request.body.decode('utf-8')
			x = json.loads(body_unicode, object_hook=lambda d: SimpleNamespace(**d))
			img_bytes = base64.b64decode((x.img).encode('utf-8'))
			img = Image.open(io.BytesIO(img_bytes))
			data = core.generate_tx(x.schedule_id,x.device_id,img)
			context = {
				"schedule_id": x.schedule_id,
				"device_id" : x.device_id,
				"response" : data
			}
		except Exception as e:
			context = {"exception" : str(e)}
			return JsonResponse(context)
		return JsonResponse(context)
	else:
		context = {
	      'response': 'requests Denied'
	       }
		return JsonResponse(context)

