import urllib.request, json, os
import time, math
from dotenv import load_dotenv
from termcolor import colored
import smtplib

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

def sendEmail(crypto, price, to):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(os.getenv('gmail_email'), os.getenv('gmail_password'))

        subject = "CryptoPY alert!"
        body = "The price of "+crypto+" has reached "+price+"€, thank you for chosing CryptoPY!"
        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            os.getenv('gmail_email'),
            to,
            msg.encode('utf-8').strip()
        )
        print("Email has been sent.")

        server.quit()

def menu():
    option = int(input("What do you want to do? \n1. Check current prices.\n2. Setup an alert.\n3. Check prices for x seconds.\n4. Simulate trading.\n5. Exit.\n"))
    if option == 1:
        print("\n")
        checkPrices()
        print("\n")

    elif option == 2:
        print("This process will run indefinitely until your alert is completed.\n")

        email = input("Introduce the email where the email will be sent to. ")
        crypto = input("Introduce the crypto you want to monitorize (BTC, ETH, XRP, XMR, USD) ")
        price = float(input("Introduce the value of the cryptocurrency you want to reach. "))
        
        if crypto.upper() == "BTC":
            stopalert = False
            while stopalert == False:
                print(colored(checkBTC(), "green"))
                print("\n")
                time.sleep(10)
                if price <= checkBTC():
                    sendEmail('BTC', str(checkBTC()), email)
                    stopalert = True
        elif crypto.upper() == "ETH":
            stopalert = False
            while stopalert == False:
                print(colored(checkETH(), "green"))
                print("\n")
                time.sleep(10)
                if price <= checkETH():
                    sendEmail('ETH', str(price), email)
                    stopalert = True
        
        
    elif option == 3:
        seconds = int(input("Enter the seconds you want to monitor the prices, keep in mind that the prices are refreshed every 10 seconds. "))
        if seconds<30:
            print("\n")
            checkPrices()
            print("\n")
        else:
            times = seconds / 10
            times = int(times)
            for i in range(0,times,1):
                print("\n")
                checkPrices()
                print("\n")
                time.sleep(10)
    elif option == 4:
        print("Entering trading simulation...\n")

        crypto = input("Introduce the crypto you want to trade with (BTC, ETH, XRP, XMR, USDT) -> ")
        sell = float(input("Enter the price whenever you want to sell your cryptocurrency (EUR) -> "))
        buy = float(input("Enter the price whenever you want to buy your cryptocurrency (EUR) -> "))
        amount = float(input("Enter the amount of crypto you want to start with (CRYPTO) -> "))
        bankroll = float(input("Enter the money you have to buy crypto (EUR) -> "))
        steps = float(input("Enter how much you want to sell each time (CRYPTO) -> "))
        buymoney = float(input("Enter how much money you want to spend buying (EUR) -> "))

        trading(crypto, sell, buy, amount, bankroll, steps, buymoney)
    elif option == 5:
       global stop
       print("See you soon!")
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
            else:
                inc = 0
            
            btcprice = float(data[i]['price'])
            if inc != 0:
                if increment == True:
                    print("BTC: "+str(btcprice) + " ↑ "+colored(str(inc) + "%", "green"))
                elif increment == False:
                    print("BTC: "+str(btcprice) + " ↓ "+colored(str(inc) + "%", "red"))
            else:
                print("BTC: "+str(btcprice) + " ~ "+colored(str(inc) + "%", "blue"))

        elif i==1:
            if float(data[i]['price']) > ethprice and ethprice != 0: 
                increment = True
                inc = ((float(data[i]['price']) / ethprice) - 1 ) * 100
            elif float(data[i]['price']) < ethprice and ethprice != 0:
                increment = False
                inc = ((float(data[i]['price']) / ethprice) - 1 ) * 100
            else:
                inc = 0

            ethprice = float(data[i]['price'])
            if inc != 0:
                if increment == True:
                    print("ETH: "+str(ethprice) + " ↑ "+colored(str(inc) + "%", "green"))
                elif increment == False:
                    print("ETH: "+str(ethprice) + " ↓ "+colored(str(inc) + "%", "red"))
            else:
                print("ETH: "+str(ethprice) + " ~ "+colored(str(inc) + "%", "blue"))
        elif i==2:
            if float(data[i]['price']) > xrpprice and xrpprice != 0: 
                increment = True
                inc = ((float(data[i]['price']) / xrpprice) - 1 ) * 100
            elif float(data[i]['price']) < xrpprice and xrpprice != 0:
                increment = False
                inc = ((float(data[i]['price']) / xrpprice) - 1 ) * 100
            else:
                inc = 0

            xrpprice = float(data[i]['price'])
            if inc != 0:
                if increment == True:
                    print("XRP: "+str(xrpprice) + " ↑ "+colored(str(inc) + "%", "green"))
                elif increment == False:
                    print("XRP: "+str(xrpprice) + " ↓ "+colored(str(inc) + "%", "red"))
            else:
                print("XRP: "+str(xrpprice) + " ~ "+colored(str(inc) + "%", "blue"))
        elif i==3:
            if float(data[i]['price']) > xmrprice and xmrprice != 0: 
                increment = True
                inc = ((float(data[i]['price']) / xmrprice) - 1 ) * 100
            elif float(data[i]['price']) < xmrprice and xmrprice != 0:
                increment = False
                inc = ((float(data[i]['price']) / xmrprice) - 1 ) * 100
            else:
                inc = 0

            xmrprice = float(data[i]['price'])
            if inc != 0:
                if increment == True:
                    print("XMR: "+str(xmrprice) + " ↑ "+colored(str(inc) + "%", "green"))
                elif increment == False:
                    print("XMR: "+str(xmrprice) + " ↓ "+colored(str(inc) + "%", "red"))
            else:
                print("XMR: "+str(xmrprice) + " ~ "+colored(str(inc) + "%", "blue"))
        elif i==4:
            if float(data[i]['price']) > usdtprice and usdtprice != 0: 
                increment = True
                inc = ((float(data[i]['price']) / usdtprice) - 1 ) * 100
            elif float(data[i]['price']) < usdtprice and usdtprice != 0:
                increment = False
                inc = ((float(data[i]['price']) / usdtprice) - 1 ) * 100
            else:
                inc = 0

            usdtprice = float(data[i]['price'])
            if inc != 0:
                if increment == True:
                    print("USTD: "+str(usdtprice) + " ↑ "+colored(str(inc) + "%", "green"))
                elif increment == False:
                    print("USTD: "+str(usdtprice) + " ↓ "+colored(str(inc) + "%", "red"))
            else:
                print("USTD: "+str(usdtprice) + " ~ "+colored(str(inc) + "%", "blue"))
def checkBTC():
    url = "https://api.nomics.com/v1/currencies/ticker?key="+os.getenv("api_key")+"&ids=BTC,ETH,XRP,XMR,USDT&interval=1d,30d&convert=EUR"
    data = json.loads(urllib.request.urlopen(url).read())

    btcprice = float(data[0]['price'])
    return btcprice
def checkETH():
    url = "https://api.nomics.com/v1/currencies/ticker?key="+os.getenv("api_key")+"&ids=BTC,ETH,XRP,XMR,USDT&interval=1d,30d&convert=EUR"
    data = json.loads(urllib.request.urlopen(url).read())

    ethprice = float(data[1]['price'])
    return ethprice
def checkXRP():
    url = "https://api.nomics.com/v1/currencies/ticker?key="+os.getenv("api_key")+"&ids=BTC,ETH,XRP,XMR,USDT&interval=1d,30d&convert=EUR"
    data = json.loads(urllib.request.urlopen(url).read())

    xrpprice = float(data[2]['price'])
    return xrpprice
def checkXMR():
    url = "https://api.nomics.com/v1/currencies/ticker?key="+os.getenv("api_key")+"&ids=BTC,ETH,XRP,XMR,USDT&interval=1d,30d&convert=EUR"
    data = json.loads(urllib.request.urlopen(url).read())

    xmrprice = float(data[3]['price'])
    return xmrprice
def checkUSDT():
    url = "https://api.nomics.com/v1/currencies/ticker?key="+os.getenv("api_key")+"&ids=BTC,ETH,XRP,XMR,USDT&interval=1d,30d&convert=EUR"
    data = json.loads(urllib.request.urlopen(url).read())

    usdtprice = float(data[4]['price'])
    return usdtprice
def convertBTCEUR(btc):
    btcvalue = checkBTC()
    return btc * btcvalue
def convertEURBTC(eur):
    btcvalue = checkBTC()
    return eur / btcvalue
def convertETHEUR(eth):
    ethvalue = checkETH()
    return eth * ethvalue
def convertEURETH(eur):
    ethvalue = checkETH()
    return eur / ethvalue
def convertXRPEUR(xrp):
    xrpvalue = checkXRP()
    return xrp * xrpvalue
def convertEURXRP(eur):
    xrpvalue = checkXRP()
    return eur / xrpvalue
def convertXMREUR(xmr):
    xmrvalue = checkXMR()
    return xmr * xmrvalue
def convertEURXMR(eur):
    xmrvalue = checkXMR()
    return eur / xmrvalue

def trading(crypto, sell, buy, amount, bankroll, steps, buymoney):
    while True:
        
        if crypto.upper() == "BTC":
            btcprice = checkBTC()
            
            if btcprice>=sell and amount>0:
                if amount - steps > 0:
                    print("Selling -> ", colored(btcprice, "green"))
                    amount -= steps
                    bankroll += convertBTCEUR(steps)
                else:
                    print(colored("Insufficient crypto to sell...\n", "red"))

                print("STATS:\namount ->",amount," \nbankroll->",bankroll)

            if buy>=btcprice and bankroll>0:
                print("Buying -> ", colored(btcprice, "red"))

                if bankroll - convertBTCEUR(steps) > 0:
                    bankroll -= convertBTCEUR(steps)
                    amount += convertEURBTC(buymoney)
                else:
                    print(colored("Insufficient funds to buy crypto...\n", "red"))

                print("STATS:\namount ->",amount," \nbankroll->",bankroll)
                
            if buy<btcprice<sell:
                print("idle -> ", colored(btcprice, "blue"))
    
            time.sleep(10)
        elif crypto.upper() == "ETH":
            ethprice = checkETH()
            
            if ethprice>=sell and amount>0:
                if amount - steps > 0:
                    print("Selling -> ", colored(ethprice, "green"))
                    amount -= steps
                    bankroll += convertETHEUR(steps)
                else:
                    print(colored("Insufficient crypto to sell...\n", "red"))

                print("STATS:\namount ->",amount," \nbankroll->",bankroll)

            if buy>=ethprice and bankroll>0:
                print("Buying -> ", colored(ethprice, "red"))

                if bankroll - convertETHEUR(steps) > 0:
                    bankroll -= convertETHEUR(steps)
                    amount += convertEURETH(buymoney)
                else:
                    print(colored("Insufficient funds to buy crypto...\n", "red"))

                print("STATS:\namount ->",amount," \nbankroll->",bankroll)

            if buy<ethprice<sell:
                print("idle -> ", colored(ethprice, "blue"))

            time.sleep(10)
        elif crypto.upper() == "XRP":
            xrpprice = checkXRP()
            
            if xrpprice>=sell and amount>0:
                if amount - steps > 0:
                    print("Selling -> ", colored(xrpprice, "green"))
                    amount -= steps
                    bankroll += convertXRPEUR(steps)
                else:
                    print(colored("Insufficient crypto to sell...\n", "red"))

                print("STATS:\namount ->",amount," \nbankroll->",bankroll)

            if buy>=xrpprice and bankroll>0:
                print("Buying -> ", colored(xrpprice, "red"))

                if bankroll - convertXRPEUR(steps) > 0:
                    bankroll -= convertXRPEUR(steps)
                    amount += convertEURXRP(buymoney)
                else:
                    print(colored("Insufficient funds to buy crypto...\n", "red"))

                print("STATS:\namount ->",amount," \nbankroll->",bankroll)

            if buy<xrpprice<sell:
                print("idle -> ", colored(xrpprice, "blue"))

            time.sleep(10)
        elif crypto.upper() == "XMR":
            xmrprice = checkXMR()
            
            if xmrprice>=sell and amount>0:
                if amount - steps > 0:
                    print("Selling -> ", colored(xmrprice, "green"))
                    amount -= steps
                    bankroll += convertXMREUR(steps)
                else:
                    print(colored("Insufficient crypto to sell...\n", "red"))

                print("STATS:\namount ->",amount," \nbankroll->",bankroll)

            if buy>=xmrprice and bankroll>0:
                print("Buying -> ", colored(xmrprice, "red"))

                if bankroll - convertXMREUR(steps) > 0:
                    bankroll -= convertXMREUR(steps)
                    amount += convertEURXMR(buymoney)
                else:
                    print(colored("Insufficient funds to buy crypto...\n", "red"))

                print("STATS:\namount ->",amount," \nbankroll->",bankroll)

            if buy<xmrprice<sell:
                print("idle -> ", colored(xmrprice, "blue"))

            time.sleep(10)
while stop != True:
    menu()
