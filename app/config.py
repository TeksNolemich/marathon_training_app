import os
import string
import random


class BaseConfig(object):
    """base config"""
    SECRET_KEY = os.environ.get("secret_key", ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in range(16)]))


class TestingConfig(BaseConfig):
    """testing config"""
    TESTING = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """dev config"""
    DEBUG = True
    MONGO_URI = '<redacted>'


class ProductionConfig(BaseConfig):
    """production config"""