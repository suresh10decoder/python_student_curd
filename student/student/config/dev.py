import os
"""Default configuration

Use env var to override
"""
DEBUG = True
SECRET_KEY = "ksr"
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1:3306')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_NAME = os.environ.get('DB_NAME', 'student_service')
SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
# SQLALCHEMY_DATABASE_URI = "mysql://root:secret@10.8.1.68:3306/prequal"
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = True
