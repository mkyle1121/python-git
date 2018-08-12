#!/bin/python3.6

import paramiko
import sys
import threading
import time
import re

class device_recv(threading.Thread):
	def __init__(self,conn):
		threading.Thread.__init__(self)
		self.conn = conn
	def run(self):
		while True:
			data=self.conn.recv(2048)
			print (data.decode(),end='')
			if not data: break

hosts_file = sys.argv[1]
commands_file = sys.argv[2]
adjusted_list_of_hosts = []
adjusted_list_of_commands = []
list_of_hosts = open(hosts_file,'r').readlines()
list_of_commands = open(commands_file,'r').readlines()
for host in list_of_hosts:
	host = host.strip('\n')
	adjusted_list_of_hosts.append(host)
for command in list_of_commands:
	command = command.strip('\n')
	adjusted_list_of_commands.append(command)
username = 'teopy'
password = 'python'
# CHANGE TO INPUT LATER
for device in adjusted_list_of_hosts:
	session = paramiko.SSHClient()
	session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	session.connect(device,username=username,password=password)
	# print ('Connecting to router '+device)
	session = session.invoke_shell()
	print ('Connected to router '+device)

	recv_thread = device_recv(session)
	recv_thread.daemon = True
	recv_thread.start()

	for command in adjusted_list_of_commands:
		# print (command.upper())
		session.sendall(command+'\n')
		# data=session.recv(2048)
		# print (data.decode())
		# if re.findall(r'Invalid input detected',data.decode()):
		# 	print ('ERROR IN COMMAND.  Execution exited...')
		# 	sys.exit()
		# print ('\nSent successful command: '+command)
	time.sleep(3)
	print ('\nSent all commands for device: '+device)
	session.close()