import pyotp
import sqlite3
import time


def generate_secret():
	return pyotp.random_base32()

def generate_bulk_fake_data(total):
	num = 0
	while num < total:
		print(f"""INSERT INTO station VALUES (‘ship_id{str(pyotp.random_base32())}′,
			station_id{str(pyotp.random_base32())},
			’berth_num{str(pyotp.random_base32())}’,
			’waterimg_{str(pyotp.random_base32())}’,
			’meterimg_{str(pyotp.random_base32())}’, 
			'before{str(pyotp.random_base32())}', 
			'after{str(pyotp.random_base32())}s');""")
		num = num + 1

def verify( num_id, otp_num, db_path ="/home/larry/Desktop/EGN Project/Dedicated Server/server/special"):
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
		return False

def main():
    generate_bulk_fake_data(30)

if __name__ == "__main__":
    main()
