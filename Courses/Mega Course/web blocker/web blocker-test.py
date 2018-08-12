import time
from datetime import datetime as dt


hosts_temp='hosts'
hosts_path="c:\windows\system32\drivers\etc\hosts"
redirect='127.0.0.1'
website_list=['www.facebook.com','facebook.com','www.youtube.com','youtube.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print ('Working Hours...')
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website+'\n')
    else:
        content=[]
        with open(hosts_temp, 'r+') as file:
            content = (file.readlines())
            for thing in content:
                print (thing)

            print('START HERE---------------------------------------------')
            for web in website_list:
                print(web)
                for item in content:
                    if web in item:
                        content.remove(item)
                        print ('removed---',item)

            for thing in content:
                print(thing)

        with open(hosts_temp, 'w') as file:
            for line in content:
                file.write(line)






            # content=file.readlines()
            # file.seek(0)
            # for line in content:
            #     if not any(website in line for website in website_list):
            #         file.write(line)
            # file.truncate()
        print ('Fun Hours...')
    time.sleep(5)