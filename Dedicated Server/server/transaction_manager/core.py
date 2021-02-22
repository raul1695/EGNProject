import pyotp
import sqlite3
import json
import itertools
import os
from time import time 
from PIL import Image
import random
import string

def convert_to_dic(cursor):
	desc = cursor.description
	column_names = [col[0] for col in desc]
	data = [dict(zip(column_names, row))  
	        for row in cursor.fetchall()]
	return data

def get_all_tx():
	try:
		db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		data = c.execute("SELECT tx_id, tx_timestamp, schedule_id FROM tx_manager")
		return convert_to_dic(data)
	except Exception as e:
		return str(e)

def generate_img_name(device_id):
	try:
		s_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
		return str(device_id)+"-"+s_string
	except Exception as e:
		raise e
		return str(e)

def schedule_pending(sch_id):
	try:
		db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		c.execute('''SELECT * FROM schedule_manager WHERE schedule_id = '{0}' and status_of_visit = "pending"; '''.format(sch_id))
		data = c.fetchall()
		if(len(data) == 0):
			return False
		else:
			return True
	except Exception as e:
		return False

def updte_schedule(schedule_id):
	try:
		db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
		conn = sqlite3.connect(db_path)
		cursor = conn.cursor()
		cursor.execute(''' UPDATE schedule_manager SET status_of_visit = "{0}" WHERE schedule_id = {1};'''.format("completed",schedule_id))
		conn.commit()
	except Exception as e:
		raise e


def generate_tx(schedule_id, device_id, img_in_PIL_format):
	if(schedule_pending(schedule_id) == False):
		raise Exception("Invalid Schedule! Must be a Pending Schedule")
	else:
		try:
			img_id = generate_img_name(device_id)
			db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
			conn = sqlite3.connect(db_path)
			c = conn.cursor()
			ts = int(time() * 1000)
			c.execute(''' INSERT INTO tx_manager(schedule_id,device_id,img_meter_id,tx_timestamp) VALUES('{0}','{1}','{2}','{3}');'''.format(schedule_id, device_id, img_id,ts))
			img_in_PIL_format.save(str(((os.path.split(os.getcwd()))[0]))+"/server/transaction_manager/img_data/"+img_id, "JPEG")
			conn.commit()
			updte_schedule(schedule_id)
			return True
		except Exception as e:
			return str(e)

