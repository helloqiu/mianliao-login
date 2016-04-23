#!/usr/bin/env python3
# coding=utf-8

import requests
import getpass

URL = "https://wifi.52mianliao.com"


def fuck_mianliao():
    print(
        " ||============================================||\n\
 ||  ______          _  __     __              || \n\
 || |  ____|        | | \ \   / /              || \n\
 || | |__ _   _  ___| | _\ \_/ /__  _   _      || \n\
 || |  __| | | |/ __| |/ /\   / _ \| | | |     || \n\
 || | |  | |_| | (__|   <  | | (_) | |_| |     || \n\
 || |_|  _\__,_|\___|_|\_\_|_|\___/ \__,_|     || \n\
 || |  \/  (_)           | |    (_)            || \n\
 || | \  / |_  __ _ _ __ | |     _  __ _  ___  || \n\
 || | |\/| | |/ _` | '_ \| |    | |/ _` |/ _ \ || \n\
 || | |  | | | (_| | | | | |____| | (_| | (_) |||\n\
 || |_|  |_|_|\__,_|_| |_|______|_|\__,_|\___/ ||\n\
 ||============================================||\n\
"
    )

if __name__ == '__main__':
    fuck_mianliao()
    username = input('username: ')
    password = getpass.getpass('password: ')
    get_mianliao = requests.get(URL, verify=False)
    if get_mianliao.status_code != 200:
        print("Can not connect to the Mianliao Auth Server!")
    headers = {'Connection': 'keep-alive',
               'Content-Length': 53,
               'Cache-Control': 'max-age=0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Origin': 'https://wifi.52mianliao.com',
               'Upgrade-Insecure-Requests': 1,
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Referer': 'https://wifi.52mianliao.com/',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
               }
    again_data = {'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
                  'sw': 1280,
                  'sh': 720,
                  'ww': 1280,
                  'wh': 720}
    post_mianliao = requests.post(URL, cookies=get_mianliao.cookies, headers=headers,
                                  data='username=%s&password=%s&action=login' % (username, password), verify=False)
    post_mianliao = requests.post(
        URL, cookies=get_mianliao.cookies, headers=headers, data=again_data, verify=False)
    if "登陆服务器响应异常" in post_mianliao.text:
        print(
            "Mianliao's login server is down! :(\nThat's why mianliao sucks :(")
        exit()
    if "登陆用户" in post_mianliao.text:
        print("login success! :)")
        exit()
    print("I don't know what's going on! :(")
    print(post_mianliao.text)
    exit()
