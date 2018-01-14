import requests, json

#r = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=XRPETH')
r = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-xrp').text
resultDict = json.loads(r)

if resultDict.success is True:
    print(resultDict.result[0].last)    
else:
    print(resultDict.message)
