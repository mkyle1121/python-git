import telnetlib
import time

username = 'teopy'
password = 'python'
HOST = '192.168.200.101'

connection = telnetlib.Telnet(HOST)

connection.read_until()
