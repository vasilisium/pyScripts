import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_links(url_main, url_all='/all/views/all/'):
    html = get_html(url_main + url_all)
    soup = BeautifulSoup(html, 'lxml')

    records = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
    links = []

    for td in records:
        a = td.find('a', class_='currency-name-container').get('href')
        links.append(url_main + a)
    return links


    #table class: table floating-header summary-table js-summary-table dataTable no-footer
    #       id: currencies-all
    # a class currency-name-container link-secondary

def get_page_data(url):
    # name: h1 class_='details-panel-item--name'
    # price
    # currency
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    name = soup.find('h1', class_='details-panel-item--name')
    return name




def main():
    url_all = '/all/views/all/'
    url_main = 'https://coinmarketcap.com'

    links = get_links(url_main, url_all=url_all)
    for i in range(0,1):
        name = get_page_data(links[i])
        print(name)


if __name__ == '__main__':
    main()