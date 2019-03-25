"""
Django settings for demo1 project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
# sys.path: python的搜索模块的路径集, 是一个list
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目根路径
# /home/python/Desktop/code/django_test/demo1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Django 自带的秘钥, 将来如果需要进行加密处理可以用此秘钥
SECRET_KEY = '(6iez(3q&2^po&auxwvrq83*3*0ha4an0nj^ff$5dr1-vo6z&e'

# SECURITY WARNING: don't run with debug turned on in production!
# 默认开启DEBUG调试模式, 将来部署上线时, 需要把DEBUG改为False
# 如果将来项目部署上线后, Django服务器不再提供对静态文件的访问支持, 因为Django服务器是动态业务逻辑服务器, 不擅长静态文件处理,
# 将来静态文件访问, 需要放到nginx静态文件服务器
DEBUG = True

# 允许哪些域名访问 Django 服务器
ALLOWED_HOSTS = []


# Application definition
# 安装或注册Django自带的子应用 及第三方或自己创建的子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 子应用可以注册也可以不注册
    'users.apps.UsersConfig',  # 注册子应用
    'request_response.apps.RequestResponseConfig',
    'classview.apps.ClassviewConfig',
    
]

# 中间件 MIDDLEWARE, 类似于flask中的请求钩子, 处理请求/响应之外的重复性操作
# 在Django使用中间件,最主要监听 请求处理前  响应
# 请求在被处理之前 所有的中间件是自上而下去执行
# 当请求被处理之后在响应时, 所有中间件的执行顺序是自下而上
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',   # CSRF 跨站请求伪造
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.my_middleware',  # 注册中间件
    'middleware.my_middleware2',  # 注册中间件
]

# 工程配置的路由入口文件
ROOT_URLCONF = 'demo1.urls'

# 模板文件配置项
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 指定模板文件 加载路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 部署上线后工程启动入口
WSGI_APPLICATION = 'demo1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 数据库配置项, 默认 sqlite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'django_demo'  # 数据库名字
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# 密码验证配置项
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# 工程语言, 默认是英文, 可以修改为简体中文, zh-hans
LANGUAGE_CODE = 'en-us'

# 时区 默认是世界时间, 可以修改为亚洲/上海时区 Asia/shanghai
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 静态文件访问的路由前缀,
STATIC_URL = '/static/'
# http://127.0.0.1:8000/static/index.html
# http://127.0.0.1:8000/static/mm03.jpg
# 配置静态文件加载存储目录
STATICFILES_DIRS = [
    # /home/python/Desktop/code/django_test/demo1/static_files
    os.path.join(BASE_DIR, 'static_files'),
    os.path.join(BASE_DIR, 'static_files/test'),
]

# 提示form的action地址最后不是/结尾的,APPEND_SLASH的值默认是 Ture
# APPEND_SLASH = False


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# session 的存储方式
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = "default"
