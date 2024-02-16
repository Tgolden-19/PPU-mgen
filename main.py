"""
The main program for running the auto generator for bot texts at Point Pickup
Created by Tristan Golden on 9/7/20
"""
from bs4 import BeautifulSoup
import requests as rq
import atlastk as Atlas
import txtmsggen as mgen

username = input('Enter your username: ')
password = input('Enter your password: ')

condi = True




while condi:
    pknum = input('Enter the full PK#: ')
    type = input('If you want to write a pub msg enter 1 \n If you want to write a pickup reminder enter 2 \n If you want to write a dropoff reminder enter 3 \n If you want to write a general point mark msg enter 4 \n If you want to write store wait msg enter 5 \n ENTER # HERE:')
    type = int(type)
    # http = urllib3.PoolManager()
    # loginpage = http.request('GET', 'https://pointpickup.com/control-panel/login')
    # login = {'panel_user' : username, 'admin_pass' : password} #creates login payload
    # data = urllib.urlencode(login)
    # session = http.request('POST', 'https://pointpickup.com/control-panel/login', data)
    # print(session)


    # username = 'tgolden@pointpickup.com' #Default username (my/the dev's username) for testing
    # password = 'TBG@pointpickup20'  #Default passsword (my/ the dev's password) for testing
    # pknum = 'PK-1583045203-3447470' #pk number for testing entry to PK
    impnums = pknum.split('-')[1:]
    PKROUTE = 'deliveries/info/PK-' + impnums[0] + '/as-it-is/' + impnums[1] + '?selectedTab=delivered'
    URL = 'https://pointpickup.com/control-panel/'
    LOGINROUTE = 'login'
    ACCROUTE = 'accounts'  # for testing login post
    HEADERS = {
        'authority': 'pointpickup.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://pointpickup.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://pointpickup.com/control-panel/login',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_ga=GA1.2.2071116604.1598475043; ci_session=1m8mahp1cgiccfa5820j83pd1es1msf2',
    }
    session = rq.session()  # starting the web session
    soup = BeautifulSoup(session.get(URL).text, 'html.parser')
    csrf_token = soup.find(name='csrf')
    login = {
        'auth': '1',
        'my_timezone': '',
        'panel_user': username,
        'admin_pass': password
    }  # creates login payload
    loginreq = session.post(URL + LOGINROUTE, headers=HEADERS, data=login)

    # session = session.get(URL + ACCROUTE) #for testing entry past login page
    session = session.get(URL + PKROUTE)
    html = session.text
    #print(html) #print to confirm entry past login into dashboard page
    if type == 1:
        print(mgen.gen_pub(html))
    elif type == 2:
        print(mgen.gen_no_geo_no_pup(html))
    elif type == 3:
        print(mgen.gen_no_geo_no_doff(html))
    elif type == 4:
        print(mgen.gen_unmrkd_pup(html))
    elif type == 5:
        print(mgen.gen_store_wait(html))
    else:
        quit()
    cont = input('Would you like to continue? (Y/N)')
    cont = cont.strip()
    if cont == 'N':
        condi = False
#print(mgen.gen_pub(html))