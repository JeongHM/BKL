import os
import redis
from flask_pymongo import PyMongo

mongo = PyMongo()
r = redis.StrictRedis(host=os.getenv('REDIS_HOST'),
                      port=os.getenv('REDIS_PORT'),
                      db=os.getenv('REDIS_DB'),
                      charset='utf-8')