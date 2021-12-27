import requests
from datetime import datetime, timedelta
import datetime
from decimal import Decimal



def changeSing(num):
    if num < 0:
        return -num
    else:
        return num

def isAbsorption(time,open,high,low,close):
        height1 = close[1] - open[1]
        height2 = close[2] - open[2]

        height1 = changeSing(height1)
        height2 = changeSing(height2)

        candles =  '\n'+time[1]+': \n'\
                   '    Открыта: '+str(open[1])+'\n'\
                   '    Закрыта: '+str(close[1])+'\n'\
                   '    Тело:'+str(height1)+'\n'+\
                    time[2]+ ': \n'+ \
                   '    Открыта : '+str(open[2])+'\n'\
                   '    Закрыта: '+str(close[2])+'\n'\
                   '    Тело: '+str(height2)

        if height1 > height2:
            if close[1] >= open[2]: # is GREEN
                # print('close1 >= open2')
                if height1 >= (high[1] - low[1] / 2):
                    return 'Заходите на повышение ▲'+candles
            elif close[1] <= open[2]: # is RED
                # print('close1 <= open2')
                if height1 >= (high[1] - low[1] / 2):
                    return 'Заходите на понижение ▼'+candles
        else:
            return 'Паттер поглощения не сработал'+candles




def stock_quotes(dateTime,data):
    timeSieries = 'Time Series FX (5min)'
    time = []
    open = []
    high = []
    low = []
    close = []
    for i in range(10):
        time.append(str(dateTime))
        open.append(Decimal(data[timeSieries][str(dateTime)]['1. open']))
        high.append(Decimal(data[timeSieries][str(dateTime)]['2. high']))
        low.append(Decimal(data[timeSieries][str(dateTime)]['3. low']))
        close.append(Decimal(data[timeSieries][str(dateTime)]['4. close']))
        dateTime = dateTime - timedelta(minutes=5)

    # print(str(time[1]),'low: '+str(low[1]),'high: '+str(high[1]),'open: '+str(open[1]),'close: '+str(close[1]))
    # print(str(time[2]),'low: '+str(low[2]),'high: '+str(high[2]),'open: '+str(open[2]),'close: '+str(close[2]))
    return str(isAbsorption(time,open,high,low,close))

def get_quotes(symbol1,symbol2):
    api_key = 'PHPGFSRYP629VYHN'
    try:
        url = 'https://www.alphavantage.co/query?' \
              'function=FX_INTRADAY&from_symbol='+symbol1+'&to_symbol='+symbol2+'&interval=5min&apikey='+api_key
        r = requests.get(url)
        data = r.json()
        lastRefresh = data['Meta Data']['4. Last Refreshed']
        lastRefresh = datetime.datetime.strptime(lastRefresh, '%Y-%m-%d %H:%M:%S')
        print(data)
    except:
        return 'Ошибка. Повторите попытку позже.'

    return str(stock_quotes(lastRefresh,data))


