import os


class Config:
    SECRET_KEY = '512C7E40538A535DCD77E74E8446BE98D336D7E58F93ABB37F4DE9AD4BC4E163'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')