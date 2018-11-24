import requests
from bs4 import BeautifulSoup
from datetime import datetime
# import re
# from multiprocessing.pool import Pool
# import Exeption

def get_html(url):
    # print(f'->getting url: {url}')
    r = requests.get(url)
    return r.text

def get_coins(url_main='https://coinmarketcap.com', url_all='/all/views/all/'):
    start = datetime.now()
    print(f'{start} -> serching for coins')
    html = get_html(url_main + url_all)
    soup = BeautifulSoup(html, 'lxml')

    coins = []
    
    records = soup.find('table', id='currencies-all').find_all('tr')
    print(f'{datetime.now()-start} -> {len(records)} coins founded')
    for record in records[1:]:
        coin = {}
        coin['#'] = record.next_element.next_element.text.strip()
        coin['name'] = record.find('td', class_='currency-name').get('data-sort')
        coin['name_short'] = record.find('td', class_='col-symbol').text
        coin['value'] = record.find('a', class_='price').text
        changes = record.find_all('td', class_='percent-change')
        coin['changes'] = []
        for change in changes:
            coin_change = {}
            period = change.get('data-timespan')
            coin_change[period] = change.text.strip()
            coin['changes'].append(coin_change)
        
        coin['market_cap'] = record.find('td', class_='market-cap').text.strip()

        coins.append(coin)
    return coins

def serch_coins():
    start = datetime.now()
    url_all = '/all/views/all/'
    url_main = 'https://coinmarketcap.com'
    limit = 50

    coins = get_coins()
    end = datetime.now()

    # for coin in coins:
    #     print(coin)
    print(f'{end-start} -> {len(coins)} coins parsed.')
    return coins

def print_coin(coin):
    print(f'''
    # {coin['#']}: {coin['name_short']} {coin['name']}
    price:   {coin['value']}
    changes: {list(coin['changes'][1].keys())[0]} {coin['changes'][1][list(coin['changes'][1].keys())[0]]}
             {list(coin['changes'][2].keys())[0]}  {coin['changes'][2][list(coin['changes'][2].keys())[0]]}
''')

def main():
    coins = serch_coins()
    
    while True:
        print('-------------------------------------------------------')
        search = input('Enter coin to serch ("BTC", "btc", "bitco"...):').lower()
        if search=='':
            break
        for coin in coins:
            if coin["name_short"].lower() == search:
                print_coin(coin) 
            if search in coin["name"].lower():
                print_coin(coin)
        

if __name__ == '__main__':
    main()
