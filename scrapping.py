{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red255\green255\blue255;\red0\green0\blue0;
\red144\green1\blue18;\red0\green0\blue109;\red19\green118\blue70;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c6275\c50196;\cssrgb\c3529\c52549\c34510;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  requests\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  bs4 \cf2 \strokec2 import\cf0 \strokec4  BeautifulSoup\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 http_proxy = \cf5 \strokec5 "http://162.214.118.137:80"\cf0 \cb1 \strokec4 \
\cb3 https_proxy = \cf5 \strokec5 "http://lum-customer-c_1b683750-zone-zone1-country-us:ktbhsk2mio4z@zproxy.lum-superproxy.io:22225"\cf0 \cb1 \strokec4 \
\cb3 proxies_dict = \{\cb1 \
\cb3     \cf5 \strokec5 "http"\cf0 \strokec4 : http_proxy,\cb1 \
\cb3     \cf5 \strokec5 "https"\cf0 \strokec4 : https_proxy\cb1 \
\cb3 \}\cb1 \
\
\cb3 response = requests.get(\cf5 \strokec5 'https://www.vons.com/shop/aisles.2053.html#'\cf0 \strokec4 , \cf6 \strokec6 proxies\cf0 \strokec4 =proxies_dict)\cb1 \
\cb3 html_code = response.text\cb1 \
\
\
\cb3 first_second_level_categories_and_subcategories = \{\}\cb1 \
\cb3 second_third_level_categories_and_subcategories = \{\}\cb1 \
\
\cb3 first_level_categories_and_subcategories = BeautifulSoup(html_code, \cf5 \strokec5 'html.parser'\cf0 \strokec4 ).find_all(\cf5 \strokec5 'div'\cf0 \strokec4 , \cf5 \strokec5 'col-12 col-sm-12 col-md-4 col-lg-4 col-xl-3'\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  first_level_category_and_subcategory \cf2 \strokec2 in\cf0 \strokec4  first_level_categories_and_subcategories:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     first_level_category = first_level_category_and_subcategory.find(\cf5 \strokec5 'h2'\cf0 \strokec4 , \cf5 \strokec5 'product-title text-uppercase'\cf0 \strokec4 ).text\cb1 \
\cb3     link_cur = \cf5 \strokec5 'https://www.vons.com'\cf0 \strokec4  + first_level_category_and_subcategory.find_all(\cf5 \strokec5 'a'\cf0 \strokec4 )[-\cf7 \strokec7 1\cf0 \strokec4 ][\cf5 \strokec5 'href'\cf0 \strokec4 ]\cb1 \
\cb3     response_cur = requests.get(link_cur, \cf6 \strokec6 proxies\cf0 \strokec4 =proxies_dict)\cb1 \
\cb3     first_level_subcategories = BeautifulSoup(response_cur.text, \cf5 \strokec5 'html.parser'\cf0 \strokec4 ).find_all(\cf5 \strokec5 'h2'\cf0 \strokec4 , \cf5 \strokec5 'aisle-category'\cf0 \strokec4 )\cb1 \
\cb3     subcategories_text = []\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  subcategory \cf2 \strokec2 in\cf0 \strokec4  first_level_subcategories:\cb1 \
\cb3         subcategories_text.append(subcategory.text)\cb1 \
\cb3     first_second_level_categories_and_subcategories[first_level_category] = subcategories_text\cb1 \
\
\cb3     second_level_categories = BeautifulSoup(response_cur.text, \cf5 \strokec5 'html.parser'\cf0 \strokec4 ).find_all(\cf5 \strokec5 'a'\cf0 \strokec4 , \cf5 \strokec5 'sbc-link'\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  second_level_category \cf2 \strokec2 in\cf0 \strokec4  second_level_categories:\cb1 \
\cb3         second_level_category_link = \cf5 \strokec5 'https://www.vons.com'\cf0 \strokec4  + second_level_category[\cf5 \strokec5 'href'\cf0 \strokec4 ]\cb1 \
\cb3         second_level_category_response = requests.get(second_level_category_link, \cf6 \strokec6 proxies\cf0 \strokec4 =proxies_dict)\cb1 \
\cb3         second_level_subcategories = BeautifulSoup(second_level_category_response.text, \cf5 \strokec5 'html.parser'\cf0 \strokec4 )\cb1 \
\cb3         third_level_categories = second_level_subcategories.find_all(\cf5 \strokec5 'span'\cf0 \strokec4 , \cf5 \strokec5 "squaredThree department-filter-aisle"\cf0 \strokec4 )\cb1 \
\cb3         subcategories_text = []\cb1 \
\cb3         \cf2 \strokec2 for\cf0 \strokec4  third_level_category \cf2 \strokec2 in\cf0 \strokec4  third_level_categories:\cb1 \
\cb3             subcategories_text.append(third_level_category.a.text[\cf7 \strokec7 0\cf0 \strokec4 :-\cf7 \strokec7 4\cf0 \strokec4 ])\cb1 \
\cb3         second_third_level_categories_and_subcategories[second_level_category[\cf5 \strokec5 'data-aisle-name'\cf0 \strokec4 ]] = subcategories_text\cb1 \
}