import requests
from time import strftime
import socket
list_id_name_page = []
count = 0
dem = 0
import os,sys,requests,threading
from time import sleep
from datetime import datetime
try:
    import requests
except:
    print("Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải... ")
    os.system("pip install requests")
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('────────────────────────────────────────────────────────────')
def idelay(o):
    while(o>0):
        o=o-1
        print(f'[MTT-TOOL][.....][{o}]','     ',end='\r');sleep(1/6)
        print(f'[MTT-TOOL][X....][{o}]','     ',end='\r');sleep(1/6)
        print(f'[MTT-TOOL][XX...][{o}]','     ',end='\r');sleep(1/6)
        print(f'[MTT-TOOL][XXX..][{o}]','     ',end='\r');sleep(1/6)
        print(f'[MTT-TOOL][XXXX.][{o}]','     ',end='\r');sleep(1/6)
        print(f'[MTT-TOOL][XXXXX][{o}]','     ',end='\r');sleep(1/6)
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    trang = "\033[1;37m"
    xanh_la = "\033[1;32m"
    xanh_duong = "\033[1;34m"
    do = "\033[1;31m"
    vang = "\033[1;33m"
    tim = "\033[1;35m"
    dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
    kt_code = "</>"
    logo=f"""

    {xanh_duong} ░██████╗░█████╗░███╗░░██╗░██████╗░
    {trang} ██╔════╝██╔══██╗████╗░██║██╔════╝░
    {vang} ╚█████╗░███████║██╔██╗██║██║░░██╗░
    {xanh_la} ░╚═══██╗██╔══██║██║╚████║██║░░╚██╗
    {tim} ██████╔╝██║░░██║██║░╚███║╚██████╔╝
    {dac_biet} ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░
    {xanh_la} </> Đăng kí kênh Youtube: Mai Thành Tiến </>
    \033[1;37m────────────────────────────────────────────────────────────
    {do}[{trang}{kt_code}{do}] {vang}TOOL BUFF VIEW STORY FACEBOOK BẰNG PRO5
    {do}[{trang}{kt_code}{do}] \033[1;35mADMIN:\033[1;36m Mai Thành Tiến (Cà Sang)
    {do}[{trang}{kt_code}{do}] \033[1;31mBOX ZALO: \033[1;33m https://zalo.me/g/mgjjie942
    {do}[{trang}{kt_code}{do}] {dac_biet}YOUTUBE:\033[1;37m https://youtube.com/@tienmai2912
    {do}[{trang}{kt_code}{do}] {xanh_la}FACEBOOK:\033[1;37m facebook.com/1275398690
    \033[1;37m────────────────────────────────────────────────────────────\n"""
  
    print(logo)

def buffview(x, thanhphan9, url_str, cookie):
    time = datetime.now().strftime("%H:%M:%S")
    uid_page = list_id_name_page[x].split('|')[0]
    name_page = list_id_name_page[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://www.facebook.com',
        'referer': url_str,
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1186',
        'x-fb-friendly-name': 'storiesUpdateSeenStateMutation',
        'x-fb-lsd': 'YCCQAywyZyd74odVp6QBrw',
        'cookie': cookie9,
    }

    data = {
        'av': uid_page,
        '__user': uid_page,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'storiesUpdateSeenStateMutation',
        'variables': '{"input":{"bucket_id":"259253279258515","story_id":"'+str(thanhphan9)+'","actor_id":"'+uid_page+'","client_mutation_id":"1"},"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '5127393270671537',
    }

    runview = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
    print(f'['+str(x+1)+'] | '+str(time)+' | SUCCESS | '+str(uid_page)+' | '+str(name_page)+'')
clear()
logo()
cookie = input('Nhập Cookie: ')
headers={
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
            'cookie': cookie,
        }
try:
    url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
    getdatainfo = requests.get(url_profile,headers=headers).text
except:
    print('COOKIE DIE, VUI LÒNG KIỂM TRA LẠI!')
try:
    fb_dtsg = getdatainfo.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
    jazoest = getdatainfo.split('{"name":"jazoest","value":"')[1].split('"},')[0]
except:
    try:
        fb_dtsg = getdatainfo.split(',"f":"')[1].split('","l":null}')[0]
        jazoest = getdatainfo.split('&jazoest=')[1].split('","e":"')[0]
    except:
        print('COOKIE DIE, VUI LÒNG KIỂM TRA LẠI!')
clear()
headers_getid = {
    'cookie': cookie, 
}
data = {
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id': '5300338636681652'
}
getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']

for i in getidpro5:
    uid_page = i['profile']['id']
    name_page = i['profile']['name']
    gomlist = f'{uid_page}|{name_page}'
    list_id_name_page.append(gomlist)
logo()    
print(f'Đã Tìm Thấy '+str(len(list_id_name_page))+' Page')
url_str = input('Nhập Link STORY: ')
thanhphan9 = url_str.split('/')[5].split('/?')[0]
thanh()
soluongview = int(input('Số View Bạn Cần Tăng: '))
thanh()
delay = int(input('Nhập Delay View: '))
for x in range(soluongview):
    dem=dem+1
    threading.Thread(target=buffview,args=(x, thanhphan9, url_str, cookie, )).start()
    idelay(delay)