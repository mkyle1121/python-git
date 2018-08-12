import re

with open('SNMP-Template.txt','r') as file:
    file_read = file.read()

#print (file_read)
#can search for multiple groups, it works differently...


a = re.findall(r"\d{4}",file_read) # SEARCH MULTIPLE STRINGS!
print(a)


arp = '22.22.22.1      0      b4:a9:5a:ff:c8:45 VLAN#222      L 10.10.10.1'

b = re.findall(r"[^c-d][1-4]\Sa[^1-8]:", arp)
b = re.findall(r"OSPF|errorStatus|Index",file_read)
b = re.findall(r"errorI?", file_read)
print (b)



