import pyotp
import sqlite3
import json
import itertools
import os

def convert_to_dic(cursor):
	desc = cursor.description
	column_names = [col[0] for col in desc]
	data = [dict(zip(column_names, row))  
	        for row in cursor.fetchall()]
	return data

def get_all_schedules():
	try:
		db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		data = c.execute("SELECT ship_id, date_of_visit, berth_id, status_of_visit FROM schedule_manager")
		return convert_to_dic(data)
	except Exception as e:
		return str(e)

def get_pending():
	try:
		db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		data = c.execute("SELECT ship_id, date_of_visit, berth_id, status_of_visit FROM schedule_manager WHERE status_of_visit = '{0}'".format("pending"))
		return convert_to_dic(data)
	except Exception as e:
		return str(e)+ "Error"

def update_status(schedule_id, new_status):
	try:
		if(int(new_status) == 0):
			new_status = "pending"
		elif(int(new_status) == 1):
			new_status = "in progress"
		elif(int(new_status) == 2):
			new_status = "completed"
		else:
			new_status = "cancelled"

		db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		c.execute(''' UPDATE schedule_manager SET status_of_visit= "{0}" WHERE schedule_id = {1};'''.format(new_status,schedule_id))
		conn.commit()
		return "success"
	except Exception as e:
		return str(e)