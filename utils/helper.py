from flask import request
import time, datetime
from utils.config import *

def getImage(config):
    if (config["redisClient"].get('image')):
        image_url = config["redisClient"].get('image').decode()
    else:
        colCount = config['collection'].count_documents({})
        if colCount != 0:
            url = config['collection'].find().sort("_id",-1).limit(1)[0]
            config["redisClient"].set('image', url['image_url'], ex=REDIS_EXPIRE_SECONDS)
            image_url = url['image_url']
        else:
            image_url = ""
    return image_url

def upload(config):
    imageObj = request.files['image']
    if imageObj.filename == '':
        return -1

    if not imageObj.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
       return -1

    imageExtension = os.path.splitext(imageObj.filename)[1]
    imagePrefix = time.time_ns()
    imageName = '{}{}'.format(imagePrefix, imageExtension)
    imagePath = os.path.join(config['UPLOAD_FOLDER'], imageName)
    imageObj.save(imagePath)
    config["s3"].Bucket(config['bucket']).upload_file(imagePath, imageName, ExtraArgs={'ContentType': imageObj.content_type, 'ACL': "public-read"})
    url = "https://{}.s3.amazonaws.com/{}".format(config['bucket'], imageName)
    config['collection'].insert_one({"image_url": url, "added": datetime.datetime.now()})
    os.remove(imagePath)

    return 0