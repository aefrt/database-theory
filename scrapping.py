import requests
from bs4 import BeautifulSoup

http_proxy = "http://162.214.118.137:80"
https_proxy = "http://lum-customer-c_1b683750-zone-zone1-country-us:ktbhsk2mio4z@zproxy.lum-superproxy.io:22225"
proxies_dict = {
    "http": http_proxy,
    "https": https_proxy
}

response = requests.get('https://www.vons.com/shop/aisles.2053.html#', proxies=proxies_dict)
html_code = response.text


first_second_level_categories_and_subcategories = {}
second_third_level_categories_and_subcategories = {}

first_level_categories_and_subcategories = BeautifulSoup(html_code, 'html.parser').find_all('div', 'col-12 col-sm-12 col-md-4 col-lg-4 col-xl-3')
for first_level_category_and_subcategory in first_level_categories_and_subcategories:
    first_level_category = first_level_category_and_subcategory.find('h2', 'product-title text-uppercase').text
    link_cur = 'https://www.vons.com' + first_level_category_and_subcategory.find_all('a')[-1]['href']
    response_cur = requests.get(link_cur, proxies=proxies_dict)
    first_level_subcategories = BeautifulSoup(response_cur.text, 'html.parser').find_all('h2', 'aisle-category')
    subcategories_text = []
    for subcategory in first_level_subcategories:
        subcategories_text.append(subcategory.text)
    first_second_level_categories_and_subcategories[first_level_category] = subcategories_text

    second_level_categories = BeautifulSoup(response_cur.text, 'html.parser').find_all('a', 'sbc-link')
    print(second_level_categories)
    for second_level_category in second_level_categories:
        print(second_level_category)
        second_level_category_link = 'https://www.vons.com' + second_level_category['href']
        second_level_category_response = requests.get(second_level_category_link, proxies=proxies_dict)
        second_level_subcategories = BeautifulSoup(second_level_category_response.text, 'html.parser')
        third_level_categories = second_level_subcategories.find_all('span', "squaredThree department-filter-aisle")
        subcategories_text = []
        for third_level_category in third_level_categories:
            subcategories_text.append(third_level_category.a.text[0:-4])
        second_third_level_categories_and_subcategories[second_level_category['data-aisle-name']] = subcategories_text
