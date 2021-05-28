import os

ENV = os.getenv('ENV', 'production')
if ENV not in ('production', 'development', 'testing'):
    raise ValueError(f"{ENV} should be 'production', 'development' or 'testing'")
DEBUG = ENV != 'production'
TESTING = ENV == 'testing'
LOG_LEVEL = os.getenv('LOG_LEVEL') or DEBUG and 'DEBUG' or 'INFO'
