from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
import os, boto3, redis, time, datetime, utils.helper as helper
from utils.config import *

app = Flask(__name__)

@app.before_first_request
def before_start():
    app.logger.info("booting application..")
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['bucket'] = S3_BUCKET
    
    uploadFolderExists = os.path.exists(app.config['UPLOAD_FOLDER'])
    if not uploadFolderExists:
        os.makedirs(app.config['UPLOAD_FOLDER'])

    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    s3 = boto3.resource('s3')
    app.config["s3"] = s3
    redisClient = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    if MONGO_POOL.lower() == "false" or MONGO_POOL == "false" or MONGO_POOL == False:
        mongoPool = ""
    else:
        mongoPool = "+srv"

    mongoClient = MongoClient("mongodb{}://{}:{}@{}/?retryWrites=true&w=majority".format(mongoPool, MONGO_USER, MONGO_PASS, MONGO_HOST))
    app.config["redisClient"] = redisClient
    app.config["mongoClient"] = mongoClient

    app.config['db'] = mongoClient[MONGO_DB]
    app.config['collection'] = app.config['db']["images"]

    
    app.logger.info("boot completed..")


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/upload', methods=['POST'])
def upload():
    status_code = helper.upload(app.config)
    return {"status_code": status_code}


@app.route('/')
def getImage():
    image_url = helper.getImage(app.config)
    return {'url': image_url}


if __name__ == '__main__':
   app.run(host=FLASK_HOST, port=FLASK_PORT, debug="on")
