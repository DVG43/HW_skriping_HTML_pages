import bs4
import requests
#from bs4 import BeautifulSoup
# ret = requests.get('https://2ip.ru/')
# print(ret.text)
# soup = BeautifulSoup(ret.text, 'html.parser')
# el = soup.find(id='d_clip_button')
# ip = el.text
# print(ip)
#Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.

url = 'https://habr.com/ru/all/page2/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    'Connection': 'keep-alive',
    'Cookie': 'feature_streaming_comments=true; _ym_d=1637177929; _ym_uid=16371779291016628682; _ga=GA1.2.1924266235.1637177929; fl=ru; hl=ru; __gads=ID=402cb6a5ec2b7959:T=1637177930:S=ALNI_MavOq58wwKxWd-rkTEn301pMrrw1A; cto_bundle=LBMr719qSkg1OHVhTlhTMXFxRDNIUzBDemVDYyUyQmFWQXZISGN2bjJmUkFjQ1dyZEo1Q01hU1c0ZTE1eG5oMzdIWEZtMUFMR2xrREx2OEVxaFBRS1JqaHBSSmZFcVRNSDN0ak5RU1Q2eExOaEZPVVZ4dmJDJTJGJTJCUjlwNnByTXdvZ2JoR3dKdnVMY0VUSkZXYW5ES012YW1hZmEweXclM0QlM0Q; visited_articles=63539:510970:301436:319164:49671; _gid=GA1.2.1230635523.1647182098; _ym_isad=2; habr_web_home_feed=/all/',
    'Host': 'habr.com',
    'Referer': 'https://habr.com/ru/all/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

KEYWORDS = ['дизайн', 'фото', 'web', 'Python *', 'SQL *', 'Java *']

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip()for hub in hubs)
    # print(hubs)
    # print()
    for hub in hubs:
        if hub in KEYWORDS:
            # print (article)
            data_ = article.find(class_="tm-article-snippet__datetime-published").attrs['datetime']
            href = article.find(class_="tm-article-snippet__hubs-item-link").attrs['href']
            url_ = url + href
            title = article.find('h2').find('span').text
            result = f'Статья {data_} - {title} - {url_}'
            print(result)

#ind(class_="tm-article-snippet__datetime-published")

