import os

REDIS_HOST=os.environ.get("REDIS_HOST", "HOST")
REDIS_PORT=os.environ.get("REDIS_PORT", 6379)
REDIS_DB=os.environ.get("REDIS_DB", 0)
REDIS_EXPIRE_SECONDS=os.environ.get("REDIS_EXPIRE_SECONDS", 3600)

MONGO_HOST=os.environ.get("MONGO_HOST", "HOST")
MONGO_DB=os.environ.get("MONGO_DB", "DB")
MONGO_USER=os.environ.get("MONGO_USER", "USER")
MONGO_PASS=os.environ.get("MONGO_PASS", "PASS")
MONGO_POOL=os.environ.get("MONGO_POOL", "true")

S3_BUCKET=os.environ.get("S3_BUCKET", "BUCKET")

UPLOAD_FOLDER=os.environ.get("UPLOAD_FOLDER", "uploads")

FLASK_HOST=os.environ.get("FLASK_HOST", "0.0.0.0")
FLASK_PORT=os.environ.get("FLASK_PORT", 5001)