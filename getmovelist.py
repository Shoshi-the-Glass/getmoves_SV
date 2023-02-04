import bs4
import requests
import csv
import os

# Gen9 attackdex のURL
url = "https://www.serebii.net/attackdex-sv/"
html = requests.get(url)
soup = bs4.BeautifulSoup(html.content, 'html.parser')
# セレクトボックスの選択肢(技データが載ってるページのURLが含まれる)を抽出
options = soup.find_all(name='option')
# 技データが載ってるページのURLを入れるリスト
values = []
# 技名を入れるリスト
names_EN = []
# URLだけ抽出してvaluesリストに入れる
for option in options:
    value = option.get('value')
    if value == None:
        continue
    values.append(value)
    name_EN = option.string
    if name_EN in ("AttackDex: A - G", "AttackDex: H - R", "AttackDex: S - Z"):
        continue
    names_EN.append(name_EN)


# CSVへの書き込み
base = os.path.dirname(os.path.abspath(__file__))
print(base)
print(os.path.join(base, '.\\moveURLs\\moveURLs.csv'))
with open(os.path.join(base, '.\\moveURLs\\moveURLs.csv'), 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['name of move', 'URL'])
    writer.writerows(zip(names_EN, values))