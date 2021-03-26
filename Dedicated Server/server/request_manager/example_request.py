""""

This is a sample request used to test the request_manager functionality. 
this program creates a valid POST request that is then processed by the request_manager module.

The request includes:

-An Image named exampleimpage.jpg
-User credentials ('user' and 'token', ship id, berth id, visit timestamp)

The request_manager processes this data, validating the transaction. 
If it's valid, it returns a copy of the request in json form (this functionality is exclusively for Debugging purposes)



"""


#Load and show an image with Pillow

from PIL import Image
import base64
import requests
import json
import time

def main():
	with open("exampleimage.jpg", "rb") as image:
		img_bytes = image.read()
	img_in_b64string = base64.b64encode(img_bytes).decode("utf8")
	data = {'user':'X962325' , 'ship_id' : '145697', 'docking_time': str(time.time()),'img' : img_in_b64string}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post('http://127.0.0.1:8080/request/transmit/', data = json.dumps(data), headers = headers)
	print(str(r.text))




if __name__ == "__main__":
    main()