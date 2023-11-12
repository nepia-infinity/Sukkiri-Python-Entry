import urllib.request
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer

def get_txt_from_aozorabunko(url):
  html = urllib.request.urlopen(url=url)
  soup = BeautifulSoup(html, "html.parser")
  sentences = soup.find("div","main_text").get_text().replace("\r", "").replace("\n", "").replace("\u3000", "")
  return sentences

url = "https://www.aozora.gr.jp/cards/000148/files/773_14560.html" # 青空文庫のURL指定、これは「こころ」
sentences = get_txt_from_aozorabunko(url)

text = sentences
for token in Tokenizer().tokenize(text):
    print(token)






