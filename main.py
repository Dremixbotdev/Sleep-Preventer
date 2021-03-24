import requests
from time import sleep

protocal = "https://"
web_list = ["coder101", "downloader101", "yohith"]
domain = ".herokuapp.com"
print("="*60)

while True:
    for i in web_list:
        requests.get(protocal + i + domain)
        print(protocal + i + domain)
    print("="*60)
    sleep(600)
