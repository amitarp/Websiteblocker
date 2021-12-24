import time
from datetime import datetime as dt

hostpath=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=['https://www.instagram.com/','instagram.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)< dt(dt.now().year,dt.now().month,dt.now().day,9):
        print("Working hours")
        with open(hostpath,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(hostpath,'r+') as file:
            content=file.read()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)

