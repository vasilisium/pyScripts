import requests
from bs4 import BeautifulSoup
from time import sleep

from notify_run import Notify

def get_html(url):
    # print(f'->getting url: {url}')
    r = requests.get(url)
    return r.text

def get_post_by_track(trackNumber):
    

    url_main = 'https://novaposhta.ua/tracking/international/cargo_number/'

    html = get_html(url_main + trackNumber)
    soup = BeautifulSoup(html, 'lxml')

    main_div = soup.find('div', class_='response')
    p = main_div.find('p')
    # print(p.text.strip())
    table = main_div.find('table',class_='tracking-int')
    trs = table.find_all('tr')
    status = trs[1].find_all('td')

    caption = trs[0].text.strip()
    status_date = status[0].text.strip()
    status_text = status[1].text.strip()

    return(caption, status_date, status_text)
    

def main():
    last_time = ''
    while(True):

        trackNumber = '959781695147'
        # print('getting track: ' + trackNumber)

        result = get_post_by_track(trackNumber)

        current_date = result[1]
        if (last_time != current_date):
            print(result[0], ':', result[1], result[2])
            notify = Notify()
            notify.send(result[2])
        # else:
        #     print('no changes')
        last_time = current_date
        sleep(60*10)



if __name__ == '__main__':
    main()
        