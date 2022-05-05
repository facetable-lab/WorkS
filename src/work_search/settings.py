import os.path
from pathlib import Path
from decouple import config

# Путь к директории с исходниками
BASE_DIR = Path(__file__).resolve().parent.parent

# Уникальный секретный ключ
SECRET_KEY = config('SECRET_KEY')

# Режим дебага
DEBUG = True

# Разрешенные хосты
ALLOWED_HOSTS = []

# Подключенные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'works_core',
    'works_accounts',
]

# Мидлвары, проход осуществляется сверху вниз по списку
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Путь к главному urls
ROOT_URLCONF = 'work_search.urls'

# Тут записаны пути, где Django ищет templates (HTML страницы)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Путь к главному wsgi
WSGI_APPLICATION = 'work_search.wsgi.application'

# Соединение с БД
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидация паролей
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

# Интернациализация
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Путь к директории со статическими файлами (CSS, JavaScript, Изображения)
STATIC_URL = 'static/'

# Тип поля PRIMARY KEY по умолчанию

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Переопределение юзера
AUTH_USER_MODEL = 'works_accounts.Subscriber'
