import requests
import time
import logging
import urllib3
########################
# Settings
'''
Cookie自行抓包
count_limit为运行次数
delay为每次运行等待时间
'''
cookie = ''
count_limit = 1
delay = 1
########################
logger = logging.StreamHandler()
# Disable warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def log_to_console():
    global logger
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger = logging.getLogger('log')
    logger.setLevel('DEBUG')
    logger.addHandler(console_handler)


def create():
    global cookie, logger
    url = "https://2021cny.coca-cola.cn/coke/dinner/create"

    payload = "{}"
    headers = {
        'Host': '2021cny.coca-cola.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'en-us',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Origin': 'https://2021cny.coca-cola.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Mobile/15E148 MicroMessenger/8.0.1(0x18000127) NetType/WIFI Language/en '
                      'miniProgram',
        'Connection': 'keep-alive',
        'Referer': 'https://2021cny.coca-cola.cn/grabLuckyBag.html',
        'Content-Length': '2',
        'Cookie': cookie
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    # print(response.content.decode('unicode_escape'))
    logger.info(response.content.decode('unicode_escape'))


def compose():
    global cookie
    url = "https://2021cny.coca-cola.cn/coke/dinner/compose"

    payload = "{}"
    headers = {
        'Host': '2021cny.coca-cola.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'en-us',
        'Content-Type': 'application/json',
        'Origin': 'https://2021cny.coca-cola.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Mobile/15E148 MicroMessenger/8.0.1(0x18000127) NetType/WIFI Language/en '
                      'miniProgram',
        'Connection': 'keep-alive',
        'Referer': 'https://2021cny.coca-cola.cn/home.html',
        'Content-Length': '2',
        'Cookie': cookie
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    logger.info(response.content.decode('unicode_escape'))


def draw_bag():
    global cookie
    url = "https://2021cny.coca-cola.cn/coke/dinner/bag/draw"

    payload = "{\"bag_id\":\"0\"}"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'en-us',
        'Content-Type': 'application/json',
        'Origin': 'https://2021cny.coca-cola.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Mobile/15E148 MicroMessenger/8.0.1(0x18000127) NetType/WIFI Language/en '
                      'miniProgram',
        'Connection': 'keep-alive',
        'Referer': 'https://2021cny.coca-cola.cn/grabLuckyBag.html?loadingLuckyBag=1',
        'Content-Length': '14',
        'Cookie': cookie
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    logger.info(response.content.decode('unicode_escape'))


if __name__ == '__main__':
    for count in range(0, count_limit):
        log_to_console()
        create()
        time.sleep(delay)
        compose()
        time.sleep(delay)
        draw_bag()
