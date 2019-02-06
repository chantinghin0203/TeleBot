import os


class Config:
    HOST = None
    TOKEN = "786280876:AAE7S9sEdzmnFcxff4otomvtYicy7JL8kuw"
    PORT = int(os.environ.get('PORT', '8443'))


class ProdConfig(Config):
    HOST = "0.0.0.0"
