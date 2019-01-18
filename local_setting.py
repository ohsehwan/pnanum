import os

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nanum', # DB명
        'USER': 'nanum', # 데이터베이스 계정
        'PASSWORD': 'nanum1234', # 계정 비밀번호
        'HOST': '114.202.247.167', # 데이테베이스 주소(IP)
        'PORT': '3306', # 데이터베이스 포트(보통은 3306)
    }
}