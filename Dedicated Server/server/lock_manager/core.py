import pyotp
import sqlite3
import os
import time

def generate_secret():
	return pyotp.random_base32()

def generate_otp(secret):
	return pyotp.TOTP(secret).now()


def generate_bulk(total):
	num = 0
	while num < total:
		print(f"INSERT INTO main(s) VALUES ('{generate_secret()}');")
		num = num + 1

def verify( num_id, otp_num):
	db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
	try:
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		n_id = (num_id,)
		otp = (otp_num,)
		c.execute("SELECT secret FROM lock_manager WHERE id = ?", n_id)
		secret = str((c.fetchone())[0])
		print(str(secret))
		totp = pyotp.TOTP(str(secret))
		print(totp.verify(str(otp_num)))
		return totp.verify(str(otp_num))

	except Exception as e:
		return str(db_path+ "\n" + "Error mesg: "+ str(e) + "\n")



def convert_to_dic(cursor):
	desc = cursor.description
	column_names = [col[0] for col in desc]
	data = [dict(zip(column_names, row))  
	        for row in cursor.fetchall()]
	return data


def get_all_lock():
	try:
		db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		data = c.execute("SELECT id, status, long, lat, lock_status FROM lock_manager")
		return convert_to_dic(data)
	except Exception as e:
		return str(e)


def check_status(num_id):
	db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
	try:
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		n_id = (num_id,)
		c.execute("SELECT lock_status FROM lock_manager WHERE id = ?", n_id)
		lock_status = int((c.fetchone())[0])
		if(abs((time.time()*1000) - lock_status) <= 30000):
			return "Open"
		else:
			return "Locked"

	except Exception as e:
		return str(db_path+ "\n" + "Error mesg: "+ str(e) + "\n")

def change_lock_state(num_id, otp_pass, tx_id = 1):
	db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/central_db.sqlite3"
	try:
		answer = verify(num_id, otp_pass)
		if(answer == True):
			lock_status = time.time() * 1000
			conn = sqlite3.connect(db_path)
			cursor = conn.cursor()
			cursor.execute(''' UPDATE lock_manager SET lock_status= "{0}", status = "{1}" WHERE id = {2};'''.format(lock_status,tx_id,num_id))
			conn.commit()
			return "Device Unlocked for 30 seconds"
		else:
			return "Invalid password. Try Again"
	except Exception as e:
		return str(db_path+ "\n" + "Error mesg: "+ str(e) + "\n")	






"""
def main():
    answer  = verify(3,34562)
    print(str(answer))

if __name__ == "__main__":
    main()

"""
