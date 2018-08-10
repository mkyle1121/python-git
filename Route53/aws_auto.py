import boto3
import sys
import time

# Create AWS Route 53 API client

client = boto3.client('route53')

# Read in arguments from command line

domain_name_file = sys.argv[1]
ip_addresses_old_file = sys.argv[2]
ip_addresses_new_file = sys.argv[3]

# Double check files

print('\n')

try:
	input(domain_name_file+' LIST OF DOMAIN NAMES? Enter or Ctrl-C')
	input(ip_addresses_old_file+' LIST OF OLD IP ADDRESSES?  Enter or Ctrl-C')
	input(ip_addresses_new_file+' LIST OF NEW IP ADDRESSES?  Enter or Ctrl-C ')
except KeyboardInterrupt:
	sys.exit()

# Open all files

open_domain_name_file = open(domain_name_file,'r')
open_ip_addresses_old_file = open(ip_addresses_old_file, 'r')
open_ip_addresses_new_file = open(ip_addresses_new_file, 'r')
open_failed_delete_names_file = open('delete_failures.txt', 'w')
open_failed_create_names_file = open('create_failures.txt', 'w')

# Create lists from input files

list_of_domain_names = open_domain_name_file.readlines()
list_of_old_ip_addresses = open_ip_addresses_old_file.readlines()
list_of_new_ip_addresses = open_ip_addresses_new_file.readlines()

# Print which conversions will occur

print('\n')

for domain_name, old_ip_address, new_ip_address in zip(list_of_domain_names, list_of_old_ip_addresses, list_of_new_ip_addresses):
	domain_name = domain_name.replace('\n', '')
	old_ip_address = old_ip_address.replace('\n', '')
	new_ip_address = new_ip_address.replace('\n', '')	
	print('[*] '+domain_name+' : '+old_ip_address+' --> '+new_ip_address)
print(str(len(list_of_domain_names))+' domain names, '+str(len(list_of_old_ip_addresses))+ ' old IPs, '+str(len(list_of_new_ip_addresses))+ ' new IPs.')
print('CONVERSION LIST COMPLETE, READY TO EXECUTE')
print('\n')
	
try:
	input('Press Enter to EXECUTE or Ctrl+C to quit: ')
except KeyboardInterrupt:
	sys.exit()
	
# Perform the conversion

for domain_name, old_ip_address, new_ip_address in zip(list_of_domain_names, list_of_old_ip_addresses, list_of_new_ip_addresses):
	domain_name = domain_name.replace('\n', '')
	old_ip_address = old_ip_address.replace('\n', '')
	new_ip_address = new_ip_address.replace('\n', '')
	try:
		client.change_resource_record_sets(HostedZoneId='Z1ESZTLUAN73VU',
		ChangeBatch={'Changes':[{'Action':'DELETE','ResourceRecordSet':{'Name':domain_name,
		'Type':'A','TTL':300,'ResourceRecords':[{'Value': old_ip_address}]}}]})
	except Exception as e: 
		#print(e)
		print('Failed to delete record: '+domain_name)
		open_failed_delete_names_file.write(domain_name+'\n')
	else: 
		print('Successfully deleted '+domain_name+' with IP address '+old_ip_address)
		try:
			client.change_resource_record_sets(HostedZoneId='Z1ESZTLUAN73VU',
			ChangeBatch={'Changes':[{'Action':'CREATE','ResourceRecordSet':{'Name':domain_name,
			'Type':'A','TTL':300,'ResourceRecords':[{'Value': new_ip_address}]}}]})
		except Exception as e:
			#print(e)
			print('Failed to create record: '+domain_name)
			open_failed_create_names_file.write(domain_name+'\n')
		else:
			print('Successfully created '+domain_name+' with IP address '+new_ip_address)
		
open_domain_name_file.close()
open_ip_addresses_old_file.close()
open_ip_addresses_new_file.close()
open_failed_delete_names_file.close()
open_failed_create_names_file.close()