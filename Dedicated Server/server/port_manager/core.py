import pyotp
import sqlite3


def generate_secret():
	return pyotp.random_base32()

def generate_otp(secret):
	return pyotp.TOTP(secret).now()


def generate_bulk(total):
	num = 0
	while num < total:
		print(f"INSERT INTO main(s) VALUES ('{generate_secret()}');")
		num = num + 1

def lookup( num_id, otp_num, db_path ="/home/larry/Desktop/EGN Project/Dedicated Server/server/special/station_status.sqlite3"):
	try:
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		n_id = (num_id,)
		otp = (otp_num,)
		c.execute("SELECT station FROM main WHERE id = ?", n_id)
		secret = str((c.fetchone())[0])
		
		return secret

	except Exception as e:
		return str(e)




def lookup():
    answer  = lookup("3",34562)
    print(str(answer))

if __name__ == "__main__":
    main()
