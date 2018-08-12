import re



# MATCH SEARCHES FROM BEGINNING ONLY
# SEARCH SEARCHES WHOLE STRING AND RETURNS FIRST MATCH
# FINDALL SEARCHES WHOLE STRING AND RETURNS ALL MATCHES

mystr = 'You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript, or PHP.'

#a = re.match(pattern, string, optional flags)

a = re.match('You', mystr)

print (a)

print(a.group())

a = re.match('you', mystr, re.I)
#re.I is ignore case

print (a.group())


mystr = 'can learn any programming language, you whether it is Python2, Python3, Perl, Java, javascript, or PHP.'

#a = re.match('you', mystr, re.I)
#print (a.group())

arp = '22.22.22.1      0      b4:a9:5a:ff:c8:45 VLAN#222      L'

a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
# r is for raw string.  for escape sequences
# () is for group
#  . = any character except newline
# + = previous expression may repeat 1 or more times
# * = 0 or more repetitions of previous character
# match until first space character occurs, since space character after the first group
#with ? , will match until space character
# with out ? , will be greedy and match spaces after
# second group -- \d means any decimal digit. 0-9
# \s matches any whitespace character.  space, tab, newline
# {} should be 2 or more  occurances of the regex preceeding curly braces (the whitespace) not typing comma should match exactly 2
# \w matches 0 or more occurances of word characters a-z A-Z 0-9 _

#print(a.group(1))

a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
print(a.group(1))
print (a.group(2))
print (a.group(3))
print (a.group(4))
print (a.group(0))

print (a.groups())   # returns tuple




a = re.findall(r"\d\d.\d{2}\.[0-9][0-9]\.[0-9]{1,3}",arp)

#\.  character escaping -- yes to a .  -- good for ?, +, () ,etc
#{} = says can occur 1,2,or3 times

print (a)

arp = '22.22.22.1      0      b4:a9:5a:ff:c8:45 VLAN#222      L 10.10.10.1'
a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})",arp)
print (a)


b = re.sub(r"\d", "7", arp)
#replace all with pattern

print (b)


timeout = 'timeout conn 2:00:00 half-closed 1:00:00 udp 0:02:00 icmp 1:00:00 rpc 1:00:00 h3'

t1 = re.match(r'(\w+)(\w)',timeout)

print (t1.group(1))
print (t1.group(2))


t2 = re.findall(r'\d{1}:\d{2}:\d{2}',timeout)
print (t2)
t3 = re.findall(r'\w{4}',timeout)
print (t3)
t3 = re.findall(r'\w{4,8}',timeout)
print (t3)
t3 = re.sub('time','hambone',timeout)
print (t3)
#t3 = re.findall(r'',timeout)
print (t3)

server = 'server-private 172.31.10.35 auth-port 1812 acct-port 1813 key 7 06233C08626B3D 10.1.1.1 154.34.57.42 1234.4567.7896.4'
s1 = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',server)
print (s1)
s1 = re.findall(r'\w{4,}\s',server)
print (s1)
s1 = re.findall(r'\w{4} \d{2,} key',server)    # find words atleast 4 in length, then a space,
                                               #  then digits atleasat 2 in length, then a space, and the word key
print (s1)
s1 = re.findall(r'key.+',server)   # match key, then any character after forever
print (s1)

s1 = re.findall(r'[0-1][7-9]1[1-3]',server)
print (s1)

s1 = re.findall(r'\w+-\w+\s\w+\.\w+\.\w+\.\w+',server)
print (s1)

s1 = re.findall(r'\w+\.\w+\.\w+\.\w+',server)
print (s1)

s1 = re.findall(r'1[6-8]\d\.\d{1,3}\.\d{1,3}\.\d{1,3}',server)
print (s1)
1












