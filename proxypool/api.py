# -*- coding: utf-8 -*-
from proxypool.db import RedisClient
import random
def get_proxies():
    db = RedisClient()
    db_proxy = db.get_all()
    return random.choice(db_proxy).decode("utf-8")

if __name__ == "__main__":
    print(get_proxies())