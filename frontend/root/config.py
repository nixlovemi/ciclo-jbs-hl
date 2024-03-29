# -*- coding: utf-8 -*-

import os

# PROD ONLY
'''
DJANGO_DEBUG = (os.environ['DJANGO_DEBUG'].lower() in ['true', '1'])
DJANGO_SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DJANGO_ALLOWED_HOSTS = (os.environ['DJANGO_ALLOWED_HOSTS'].split(','))
DJANGO_STATIC_ROOT = os.environ['DJANGO_STATIC_ROOT']
DJANGO_MEDIA_ROOT = os.environ['DJANGO_MEDIA_ROOT']
DJANGO_LOG_FILENAME = os.environ['DJANGO_LOG_FILENAME']
DJANGO_LOG_LEVEL = os.environ['DJANGO_LOG_LEVEL']
DJANGO_LOG_HANDLER = os.environ['DJANGO_LOG_HANDLER']

MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_DB = os.environ['MYSQL_DB']
MYSQL_PORT = os.environ['MYSQL_PORT']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWD = os.environ['MYSQL_PASSWD']

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = int(os.environ['EMAIL_PORT'])
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = (os.environ['EMAIL_USE_TLS'].lower() in ['true', '1'])
EMAIL_USE_SSL = (os.environ['EMAIL_USE_SSL'].lower() in ['true', '1'])
'''

# LOCAL ONLY
DJANGO_DEBUG = True
DJANGO_SECRET_KEY = '%*x85+-=b(h7k#7(^=qbm3#xil5__0jfzr@*zjnrdkk*l(32=h'
DJANGO_ALLOWED_HOSTS = ['127.0.0.1']
DJANGO_STATIC_ROOT = './webapp/static/'
DJANGO_MEDIA_ROOT = './webapp/media/'
DJANGO_LOG_FILENAME = './frontend.log'
DJANGO_LOG_LEVEL = 'INFO'
DJANGO_LOG_HANDLER = 'logfile'

MYSQL_HOST = '172.17.0.1'
MYSQL_DB = 'higienelimpeza'
MYSQL_PORT = 3306
MYSQL_USER = 'higienelimpeza'
MYSQL_PASSWD = 'HZhHjhT8jYJ23g7A'

EMAIL_HOST = 'in-v3.mailjet.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '21ea3371a359b90be09c731c36bd2547'
EMAIL_HOST_PASSWORD = '583a3b5846f85cd3364e8df4c8e39448'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_FROM = 'uboi.contato@gmail.com'
EMAIL_TO='comercial.hl@jbs.com.br'

GTM_CODE = 'GTM-XXXX'