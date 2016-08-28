#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import getpass
import logging

logging.basicConfig(level=logging.INFO)

URL = "https://wifi.52mianliao.com"
HEADERS = {'Connection': 'keep-alive',
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

DATA = {
    'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    'sw': 1280,
    'sh': 720,
    'ww': 1280,
    'wh': 720}


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
    s = requests.Session()
    status_code = s.get(URL, verify=False).status_code
    if status_code != 200:
        logging.info("Can not connect to the Mianliao Auth Server!")
        logging.info("Status Code: %d" % status_code)
        exit()

    s.post(URL, headers=HEADERS,
           data='username=%s&password=%s&action=login' % (username, password),
           verify=False)
    post_mianliao = s.post(URL, headers=HEADERS, data=DATA, verify=False)
    if "登陆服务器响应异常" in post_mianliao.text:
        logging.info("Mianliao's login server is down! :(\nThat's why mianliao sucks :(")
        exit()
    if "登陆用户" in post_mianliao.text:
        logging.info("login success! :)")
        exit()
    logging.info("I don't know what's going on! :(")
    logging.info(post_mianliao.text)
    exit()
