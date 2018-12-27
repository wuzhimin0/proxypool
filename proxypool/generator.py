# -*- coding: utf-8 -*-
from proxypool.db import RedisClient
from proxypool.settings import *
from lxml import etree
import requests,time
class Generator(object):
    def __init__(self):
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
        }
    def xichi_proxy(self):
        db = RedisClient()
        response = requests.get("https://www.xicidaili.com/nn/", headers=self.headers)
        ip_xml = etree.HTML(response.content)
        infos = ip_xml.xpath('//table[@id="ip_list"]/tr')[1:]
        for info in infos:
            ip = info.xpath('td[2]/text()')[0]
            port = info.xpath('td[3]/text()')[0]
            type = info.xpath('td[6]/text()')[0]
            proxy = type + "://" + ip + ":" + port
            if self.judge_proxy(proxy.lower()):
                db.put(proxy.lower())
                print("valid proxy: %s" % (proxy.lower()))
                if db.db_len() > PROXY_MAX_NUMBER:
                    break
            else:
                print("invalid proxy: %s" % (proxy.lower()))
        time.sleep(5)
    def judge_proxy(self,proxy):
        try:
            judge_result = requests.get(r"http://www.baidu.com",proxies={"http":proxy},timeout=3)
            if judge_result.status_code == 200:
                return True
            else:
                return False
        except:
            return False