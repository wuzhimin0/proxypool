# -*- coding: utf-8 -*-
from proxypool.settings import HOST,PORT,PASSWORD
import redis
class RedisClient(object):
    def __init__(self,host=HOST,port=PORT):
        if PASSWORD:
            self.db = redis.Redis(host=host,port=port,password=PASSWORD)
        else:
            self.db = redis.Redis(host=host,port=port)
    def get(self):
        proxies = self.db.lrange("proxy",0,0)
        self.db.ltrim("proxy",1,-1)
        return proxies
    def get_all(self):
        return self.db.lrange("proxy",0,self.db_len())
    def put(self,proxy):
        self.db.rpush("proxy",proxy)
    def db_len(self):
        return self.db.llen("proxy")
if __name__ == "__main__":
    print("place running run.py")