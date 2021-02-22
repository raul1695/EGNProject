from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import io
import base64
from PIL import Image
from types import SimpleNamespace

"""

This api method takes a POST HTTPS request. The api expects an http payload in json form that includes: 

- name/id of the ship
- time of docking
- id of locking device/station
- an image in byte form (base64 encoded)


"""

@csrf_exempt
def send_req(request):
	if(request.method == 'POST'):
		try:
			body_unicode = request.body.decode('utf-8')
			x = json.loads(body_unicode, object_hook=lambda d: SimpleNamespace(**d))
			img_bytes = base64.b64decode((x.img).encode('utf-8'))
			img = Image.open(io.BytesIO(img_bytes))
			context = {
				"user" : x.user,
				"ship_id": x.ship_id,
				"docking_time" : x.docking_time,
				"img_raw" : str(x.img)
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

"""
	if request.method == 'POST':
		return render(request,access_key)
	else:
		return render(request,access_key)
"""