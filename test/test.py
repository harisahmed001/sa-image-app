import unittest, utils.helper as helper, redis
from pymongo import MongoClient
from utils.config import *

class TestStringMethods(unittest.TestCase):

    def test_image(self):
        config = {}
        redisClient = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        if MONGO_POOL.lower() == "false" or MONGO_POOL == "false" or MONGO_POOL == False:
            mongoPool = ""
        else:
            mongoPool = "+srv"
        mongoClient = MongoClient("mongodb{}://{}:{}@{}/?retryWrites=true&w=majority".format(mongoPool, MONGO_USER, MONGO_PASS, MONGO_HOST))
        config["redisClient"] = redisClient
        config["mongoClient"] = mongoClient
        config['db'] = mongoClient[MONGO_DB]
        config['collection'] = config['db']["images"]
        url = helper.getImage(config)
        if (url or url==""):
            #self.assepassrtTrue(True)
            assert True
        else:
            assert False, "url not returned"

if __name__ == '__main__':
    unittest.main()