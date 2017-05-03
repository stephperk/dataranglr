import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '@{-\n\xbfJ\xa1\x04.\xd9\x1e\x9d$W<\x98\xc2f,\x96\x9e\xe9\x87\x90'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SUBJECT_PREFIX = '[DataRanglr] '
    MAIL_SENDER = 'Stephen Perkins <sperk434@gmail.com>'
    SITE_ADMIN = 'sperk434@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'sperk434@gmail.com'
    MAIL_PASSWORD = '$kittle$'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
