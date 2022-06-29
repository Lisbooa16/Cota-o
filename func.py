import datetime
import time

from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime
import requests

class Cotacao:
    def __init__(self, moeda):
        self.moeda = moeda


    def cotacao(self):
        url = f'https://www.remessaonline.com.br/cotacao/cotacao-{self.moeda}'
        hora = str(datetime.now().time())[:8]
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, "html.parser")

        dom = etree.HTML(str(soup))
        preco = dom.xpath('//*[@id="root"]/div[2]/div/div[1]/div/div[1]')[
            0].text
        time.sleep(1)
        return f'1 {self.moeda} custa {preco} na hora {hora}'
