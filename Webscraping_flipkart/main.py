#This is a simple program to get details of Apple iPhone 11 from Flipkart

#import all required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

#set the main url to add it to the productLinks @1
mainurl = 'https://www.flipkart.com'

#this is the url we are scraping
url = 'https://www.flipkart.com/mobiles/~cs-ftksk35qsu/pr?sid=tyy%2C4io&collection-tab-name=iPhone+11&sort=price_asc&param=987&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=99393&otracker=clp_banner_1_7.bannerX3.BANNER_mobile-phones-store_81UVXRZH5MST&fm=neo%2Fmerchandising&iid=M_473c0755-4f3e-4f1a-9532-ff6bad23272f_7.81UVXRZH5MST&ppt=hp&ppn=homepage&ssid=b1nlyhfi8w0000001615959155945'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

productlinks = []
productdict_list = []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
productlist = soup.find_all('div', class_='_1AtVbE col-12-12')

for item in productlist:
    for link in item.find_all('a', href=True):

        # to avoid unnecessary links check a specific word that you need in the link
        if "apple" in link['href']:
            productlinks.append(
                mainurl + link['href']
            )  #main url added to the product link as mentioned in 1
kk = 1

#traversing through each link and obtain the necessary details
for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    model = (soup.find('span', class_="B_NuCI").text)
    price = soup.find('div', class_="_30jeq3 _16Jk6d")
    print(f"saving {kk} ")  #just to make sure the code is running successfully
    kk += 1
    detail_dict = {'model': model, 'price': price}

    productdict_list.append(detail_dict)

df = pd.DataFrame(productdict_list)

print(df)
print('')
print('-------------------------')