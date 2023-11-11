# import requests
# response = requests.get('https://www.python.org/downloads/')
# text     = response.text
# print(text)

import urllib.request

url      = 'https://blog.python.org/'
requests = urllib.request.Request(url)
with urllib.request.urlopen(requests) as response:
    body = str(response.read())

if 'security' in body or 'vulnerability' in body:
    print('セキュリティに関する記述があります')
    print('https://blog.python.org/を確認してください')
else:
    print('調査対象のセキュリティ用語はありませんでした')