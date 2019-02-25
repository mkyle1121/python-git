import serial
import sys

with open (sys.argv[1]) as ali_file_open:
	ali_file_list = ali_file_open.readlines()
	ser = serial.Serial('COM4')
for send_line in ali_file_list:
	send_line= send_line.rstrip('\n')
	send_line = send_line+'\n'
	send_line = send_line+'\r'
	print(str.encode(send_line))
	ser.write(str.encode(send_line))
ser.close()