import requests
import time
from datetime import datetime

i=1
todaytime = datetime.now()
d8 = todaytime.strftime("%d.%m.%Y %H:%M")


#User will choose an amount of minutes (N) between every notification of new crpyto value so time.sleep(N)
#User will also choose which crypto value to be returned so every crypto will have its function called
#depending on what the user chose def bitcoin(): / def ethereum(): / def xrp():



#BITCOIN VALUE RETURN
while True:
    time.sleep(10*60)
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    print('The current price of Bitcoin at '+ d8 +' is: $'+r.json()['bpi']['USD']['rate'])
    i+=1
    if i>999:
        break

#ETHEREUM VALUE RETURN

#XRP VALUE RETURN








