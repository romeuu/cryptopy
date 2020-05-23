import urllib.request, json, os
import time
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

url = "https://api.nomics.com/v1/currencies/ticker?key="+os.getenv("api_key")+"&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR"


def myfn():
    data = json.loads(urllib.request.urlopen(url).read())
    
    for i in range(0,3,1):
        print(data[i]['id']+'->'+data[i]['price'])

while True:
    myfn()
    time.sleep(5)