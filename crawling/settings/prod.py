from crawling.settings import *

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "crawlingpostgres"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'crawling',
        'USER' : 'jyothinaidu94',
        'PASSWORD' : 'jnaidu2010',
        'HOST' : 'crawlingpostgres.cg3lpwl4iwlm.ap-south-1.rds.amazonaws.com',
        'PORT' : '5432',
    }
}