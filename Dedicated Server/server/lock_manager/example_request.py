import pyotp
import sqlite3
import time

"""


This is a sample program to test the Lock Manager functionality. 

This sample program attempts to open the water station with ID 37.

To test this program access the lock manager api and enter num_id = 37, otp_pass = key.now(). 

Key.now() is printed onto the screen by the program every 5 seconds. 


"""

def main():
    key  = pyotp.TOTP("UIBCKYEHOL6QATMP")
    print("The secret for this session is " + (str(key)))
    while(True):
    	print(str(key.now()))
    	time.sleep(5)

if __name__ == "__main__":
    main()
