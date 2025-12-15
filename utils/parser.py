import json

import requests
from bs4 import BeautifulSoup

url = 'https://anekdotbar.ru/dlya-detey/'

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

content = soup.find('div', id='dle-content')
items = content.find_all('div', class_='tecst')
result = []

for item in items:
    item = item.replace_with(item.find('div'), '').get_text()
    result.append(item)

with open('../jokes.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
