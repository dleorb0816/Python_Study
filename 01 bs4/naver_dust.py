from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://www.melon.com/chart/index.htm')
#pprint(html.text)

soup = bs(html.text,'html.parser')
data1 = soup.findAll('div', "wrap") # 영역 추출
pprint(data1)

#data2 = soup.findall('td', "lst50")
#pprint(data2)