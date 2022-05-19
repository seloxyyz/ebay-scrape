from bs4 import BeautifulSoup
import requests

url = 'https://www.ebay.de/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=yugioh+lob+1st+edition&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=yugioh+lob++booster+1st+ed&LH_Complete=1&LH_Sold=1'


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        products = {
            'title': item.find('h3', {'class': 's-item__title s-item__title--has-tags'}).text,
            'soldprice': item.find('span', {'class': 's-item__price'}).text,
            'solddate': item.find('span', {'class': 's-item__title--tagblock__COMPLETED'}).text,
            'link': item.find('a', {'class': 's-item__link'})['href'],
        }
        print(products)
    return


soup = get_data(url)
parse(soup)
