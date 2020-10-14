import time
from datetime import datetime as dt
import platform
curr_sys = platform.system()

hosts_path = r'C:\Windows\System32\drivers\etc\hosts' if curr_sys == 'Windows' else r'/etc/hosts'
hosts_tmp = 'hosts'
redirect = '127.0.0.1'
website_list = ['facebook.com']
s, e = 8, 18
start_time = dt(dt.now().year, dt.now().month, dt.now().day, s)
end_time = dt(dt.now().year, dt.now().month, dt.now().day, e)
while True:
    curr_time = dt.now()
    if start_time < curr_time < end_time:
        print("Working hours")
        with open(hosts_path, 'r+') as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect + ' ' + website + '\n')
    else:
        
        with open(hosts_path, 'w') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
            f.truncate()
    time.sleep(5)