import urllib.request, json, os
import time, math
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

url = "https://api.nomics.com/v1/currencies/ticker?key="+os.getenv("api_key")+"&ids=BTC,ETH,XRP,XMR,USDT&interval=1d,30d&convert=EUR"

stop = False

def menu():
    option = int(input("What do you want to do? \n1. Check current prices.\n2. Setup an alert.\n3. Check prices for x seconds.\n4. Exit.\n"))
    if option == 1:
        print("\n")
        checkPrices()
        print("\n")
    elif option == 2:
        print("Alerts are in process, they will be out soon\n")
    elif option == 3:
        seconds = int(input("Enter the seconds you want to monitor the prices, keep in mind that the prices are refreshed every 30 seconds. "))
        if seconds<30:
            print("\n")
            checkPrices()
            print("\n")
        else:
            times = seconds / 30
            times = int(times)
            for i in range(0,times,1):
                print("\n")
                checkPrices()
                print("\n")
                time.sleep(30)
    elif option == 4:
       global stop
       stop = True
        
def checkPrices():
    data = json.loads(urllib.request.urlopen(url).read())
    for i in range(0,5,1):
        print(data[i]['id']+'->'+data[i]['price'])

while stop != True:
    menu()
