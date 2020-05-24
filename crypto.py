import urllib.request, json, os
import time, math
from dotenv import load_dotenv
from termcolor import colored

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

url = "https://api.nomics.com/v1/currencies/ticker?key="+os.getenv("api_key")+"&ids=BTC,ETH,XRP,XMR,USDT&interval=1d,30d&convert=EUR"

stop = False
increment = False
inc = 0
btcprice = 0
ethprice = 0
xrpprice = 0
xmrprice = 0
usdtprice = 0

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
        global btcprice, ethprice, xrpprice, xmrprice, usdtprice, increment, inc
        if i==0:
            if float(data[i]['price']) > btcprice and btcprice != 0: 
                increment = True
                inc = ((float(data[i]['price']) / btcprice) - 1 ) * 100
            elif float(data[i]['price']) < btcprice and btcprice != 0:
                increment = False
                inc = ((float(data[i]['price']) / btcprice) - 1 ) * 100
            
            btcprice = float(data[i]['price'])
            if increment == True:
                print(str(btcprice) + " ↑ "+colored(str(inc), "green"))
            elif increment == False:
                print(str(btcprice) + " ↓ "+colored(str(inc), "red"))

        elif i==1:
            if float(data[i]['price']) > ethprice and ethprice != 0: 
                increment = True
                inc = ((float(data[i]['price']) / ethprice) - 1 ) * 100
            elif float(data[i]['price']) < ethprice and ethprice != 0:
                increment = False
                inc = ((float(data[i]['price']) / ethprice) - 1 ) * 100

            ethprice = float(data[i]['price'])
            if increment == True:
                print(str(ethprice) + " ↑ "+colored(str(inc), "green"))
            elif increment == False:
                print(str(ethprice) + " ↓ "+colored(str(inc), "red"))
        elif i==2:
            xrpprice = data[i]['price']
        elif i==3:
            xmrprice = data[i]['price']
        elif i==4:
            usdtprice = data[i]['price']
        #print(data[i]['id']+'->'+data[i]['price'])

while stop != True:
    menu()
