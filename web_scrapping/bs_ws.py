import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
path = sys.path[0]


property_list = []
base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="
header = {
    'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get(base_url, headers=header)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
page_num = int(soup.find_all('a', {'class': 'Page'})[-1].text)


def extracting(url):
    r = requests.get(url, headers=header)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    a = soup.find_all('div', {'class': 'propertyRow'})
    for item in a:
        d = {}
        d['Address'] = item.find_all(
            'span', {'class': 'propAddressCollapse'})[0].text
        d['Locality'] = item.find_all(
            'span', {'class': 'propAddressCollapse'})[1].text
        d['Price'] = item.find(
            'h4', {'class': 'propPrice'}).text.replace('\n', '').strip()
        add_dict(d, 'Beds', item, 'infoBed')
        add_dict(d, 'Area (in Sq. Ft)', item, 'infoSqFt')
        add_dict(d, 'Full Bath', item, 'infoValueFullBath')
        add_dict(d, 'Half Bath', item, 'infoValueHalfBath')
        d['Lot Size'] = None
        for column_group in item.find_all('div', {'class': 'columnGroup'}):
            for feature_group, feature_name in zip(column_group.find_all('span', {'class': 'featureGroup'}), column_group.find_all('span', {'class': 'featureName'})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text.replace(
                        ',', '').replace('s', '').replace('1/2', '0.5').replace('Under', '<').strip()
                    break

        property_list.append(d)


def add_dict(d, key, item, item_name):
    try:
        d[key] = item.find('span', {'class': item_name}).find('b').text
    except AttributeError:
        d[key] = None


for page in range(0, page_num * 10, 10):
    url = base_url + str(page) + '.html'
    extracting(url)
df = pd.DataFrame(property_list)
df.to_csv(path + '\\RealEstate.csv')
