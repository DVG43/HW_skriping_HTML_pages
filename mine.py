import requests
from bs4 import BeautifulSoup
ret = requests.get('https://2ip.ru/')
print(ret.text)
soup = BeautifulSoup(ret.text, 'html.parser')
el = soup.find(id='d_clip_button')
ip = el.text
print(ip)