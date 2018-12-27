# -*- coding: utf-8 -*-
from proxypool.db import RedisClient
from proxypool.settings import *
import requests,time
class Tester(object):
    def __init__(self):
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
        }
    def judge_proxy(self,proxy):
        try:
            judge_result = requests.get(r"http://www.baidu.com",proxies={"http":proxy},timeout=3)
            if judge_result.status_code == 200:
                return True
            else:
                return False
        except:
            return False
    def valid_proxy(self):
        print("valid_proxy working")
        db = RedisClient()
        while True:
            for i in range(db.db_len()):
                proxy = db.get()[0].decode("utf-8")
                if self.judge_proxy(proxy):
                    db.put(proxy)
                    print("valid proxies: %s"%(proxy))
                else:
                    print("invalid proxies: %s"%(proxy))
            time.sleep(JUDGE_PROXY_VALID)