import datetime
import serial
from datetime import date


ser = serial.Serial('/dev/cu.usbserial-1410', 9600)

while 1:
    print("Enter 0 or 1")
    val = input()
    if val == '1':
        now = datetime.datetime.now()
        time_str = "time {}!{}@{}#{}${}%{}^{}&".format(now.second, now.minute, now.hour, date.today().isoweekday(), now.day, now.month, now.year)
        ser.write(str.encode(time_str))

    if val == '0':
        ser.write(b"time 0")
