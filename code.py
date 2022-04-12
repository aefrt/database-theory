import requests
from bs4 import BeautifulSoup
from lxml import etree
from io import StringIO, BytesIO

response = requests.get('https://www.vons.com/shop/aisles.2053.html')
html_code = response.text

parser = etree.HTMLParser()
tree = etree.parse(StringIO(html_code), parser)

categories = tree.xpath('//div[@class="col-12 col-sm-12 col-md-4 col-lg-4 col-xl-3"]')  # 1st level
categories1 = dict()
for category in categories:
    name = category.xpath('./a/div/h2/text()')[0]  # list of 1 element -> 1 this element
    link = category.xpath('./a/@href')[0]
    categories1[name] = link
print(categories1)

for category1 in categories1.keys():  # 2nd level categories
    categories2 = dict()
    print("CATETETETETTE", category1)
    response1 = requests.get('https://www.vons.com' + categories1[category1])
    html_code1 = response1.text
    print('https://www.vons.com' + categories1[category1])
    html_code1 = response1.text
    tree1 = etree.parse(StringIO(html_code1), parser)
    categories22 = tree1.xpath('//div[@class="categories-item aisle-item "] | //div[@class="categories-item aisle-item hidden-aisle d-none"]')
    categories_22 = dict()
    print("zzz:", categories22)
    for category2 in categories22:  # 3rd level categories
        name = category2.xpath('./a/@data-aisle-name')[0]
        link = category2.xpath('./a/@href')[0]
        print("xxx:", name, link)
        categories_22[name] = link
    for categories2 in categories_22.keys():  # items
        print("amamam", 'https://www.vons.com' + categories_22[categories2])
        response2 = requests.get('https://www.vons.com' + categories_22[categories2])
        html_code2 = response2.text
        tree2 = etree.parse(StringIO(html_code2), parser)
        categories33 = tree2.xpath('//a[@class="product-title"]')
        for category3 in categories33:
            print(category3.xpath('./text()')[0][33:-29])  # костыль чтобы убрать пробелы перед названием продукта и после него
            print(category3.xpath('./@href')[0])
