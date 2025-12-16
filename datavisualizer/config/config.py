import json
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class AppConfig(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "7d4asdasda4fffa1afa27d4asd41f27567d441f2b6176a"
    DEBUG = True
    CSRF_ENABLED = True
