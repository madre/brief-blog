#coding=utf-8
"""
__create_time__ = '13-10-14'
__author__ = 'Madre'
"""
MEDIA_URL = 'http://brief-media.stor.sinaapp.com/'

# sae的本地文件系统是只读的，修改django的file storage backend为Storage
DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'
# 使用media这个bucket
STORAGE_BUCKET_NAME = 'media'
# ref: https://docs.djangoproject.com/en/dev/topics/files/

import sae.const

MYSQL_DB = sae.const.MYSQL_DB      # 数据库名
MYSQL_USER = sae.const.MYSQL_USER    # 用户名
MYSQL_PASS = sae.const.MYSQL_PASS    # 密码
MYSQL_HOST = sae.const.MYSQL_HOST    # 主库域名（可读写）
MYSQL_PORT = sae.const.MYSQL_PORT    # 端口，类型为<type 'str'>，请根据框架要求自行转换为int
MYSQL_HOST_S = sae.const.MYSQL_HOST_S  # 从库域名（只读）

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     MYSQL_DB,
        'USER':     MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST':     MYSQL_HOST,
        'PORT':     MYSQL_PORT,
    }
}