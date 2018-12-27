# -*- coding: utf-8 -*-
from proxypool.db import RedisClient
from proxypool.settings import *
from proxypool.generator import Generator
from proxypool.tester import Tester
from multiprocessing import Process
import time
class GetProxies(object):
    def get_proxy(self):
        db = RedisClient()
        while True:
            db_len = db.db_len()
            if db_len < PROXY_MIN_NUMBER:
                Generator().xichi_proxy()
            elif db_len > PROXY_MAX_NUMBER:
                time.sleep(JUDGE_PROXY_NUMBER)
            else:
                time.sleep(JUDGE_PROXY_NUMBER)
    def run(self):
        print("ip processing working")
        get_process = Process(target=self.get_proxy)
        valid_process = Process(target=Tester().valid_proxy)
        get_process.start()
        valid_process.start()