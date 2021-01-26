""""

In this document we will draft our sample https request in order to test some functionality.

in this very directory we also have an example image to use.

"""


#Load and show an image with Pillow

from PIL import Image
import base64
import requests
import json


def main():
	with open("exampleimage.jpg", "rb") as image:
		b64string = base64.b64encode(image.read())
	data = {'user':'wewewe' , 'hassssh' : 'fgfgffggfgf', 'img' : b64string.decode()}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post('http://127.0.0.1:8000/request/transmit/', data = json.dumps(data), headers = headers)
	print(str(r.text))




if __name__ == "__main__":
    main()