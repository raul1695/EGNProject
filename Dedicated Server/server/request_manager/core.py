#core

import sqlite3
import os


#Method use to verify the request comes from a valid user





#Method use to store the recieved data
def store(json_list):
	db_path = str(((os.path.split(os.getcwd()))[0]))+ "/server/data/request_manager.sqlite3"
	try:
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		n_id = (num_id,)
		otp = (otp_num,)
		c.execute("SELECT s FROM main WHERE id = ?", n_id)
		secret = str((c.fetchone())[0])
		print(str(secret))
		totp = pyotp.TOTP(str(secret))
		print(totp.verify(str(otp_num)))
		return totp.verify(str(otp_num))

	except Exception as e:
		return str(db_path+ "\n" + "Error mesg: "+ str(e) + "\n")
