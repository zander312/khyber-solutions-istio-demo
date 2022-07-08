import time
import requests


def requestor():
    r = requests.get('https://ifconfig.io/all.json')
    print(r.json())


def scheduler():
    while True:
        time.sleep(1)
        requestor()


scheduler()


