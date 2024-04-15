import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

date = [1070211600, 1082221200, 1094230800, 1106240400, 1118250000, 1130259600, 1142269200, 1154278800,
        1166288400, 1178298000, 1190307600, 1202317200, 1214326800, 1226336400, 1238346000, 1250355600,
        1262365200, 1274374800, 1286384400, 1298394000, 1310403600, 1322413200, 1334422800, 1346432400,
        1358442000, 1370451600, 1382461200, 1394470800, 1406480400, 1418490000, 1430499600, 1442509200,
        1454518800, 1466528400, 1478538000, 1490547600, 1502557200, 1514566800, 1526576400, 1538586000,
        1550595600, 1562605200, 1574614800, 1586624400, 1598634000, 1610643600, 1622653200, 1634662800,
        1646672400, 1658682000, 1670691600]

data = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

for i in range(len(date)-1):
    url = f'https://finance.yahoo.com/quote/KHR%3DX/history?period1={date[i]}&period2={date[i+1]}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
    req = Request(url=url, headers=headers)
    web = urlopen(req).read()
    soup = BeautifulSoup(web, 'lxml')

    table = soup.find('table', {'class': 'W(100%) M(0)'})
    for row in table.find_all('tr')[1:-1]:
        td_tags = row.find_all('td')
        td_vals = [y.text for y in td_tags]
        data.append(td_vals)

df = pd.DataFrame(
    data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
# df.to_csv('RielToUSD_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')
df.to_csv('RielToUSD_data_V2.csv', index=True)
