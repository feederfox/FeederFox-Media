
"""
Django settings for Feederfox project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))

#EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'help.feederfox@gmail.com'
EMAIL_HOST_PASSWORD = 'Feederfox@1234'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(+lc+x&n-r9_17saz*#avru-rt-+!t_mgn47&s%faqadyk%tjm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'accounts',
    'NewsFeeds',
    'crispy_forms',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'widget_tweaks',
    'contents',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django_rest_passwordreset',
    'social_django',
    'rest_social_auth',
    'paypal.standard.ipn',
    'payments',
    'star_ratings',
]


AUTHENTICATION_BACKENDS = (
	'social_core.backends.open_id.OpenIdAuth',  
 	'social_core.backends.google.GoogleOpenId',
 	'social_core.backends.google.GoogleOAuth2',
	'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',



)



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Feederfox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', 
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Feederfox.wsgi.application'


REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 
        'contents.serializers.ForgotPasswordSerializer',
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'


LOGIN_URL = 'accounts/login'

LOGIN_REDIRECT_URL = '/dashboard/'

LOGOUT_URL = '/home/'

FRONTEND_URL = 'http://127.0.0.1:8000/'
ACCOUNT_EMAIL_CONFIRMATION_URL = FRONTEND_URL + 'verify-email/{}'
ACCOUNT_PASSWORD_RESET_CONFIRM = FRONTEND_URL + 'password-reset/confirm/'

SOCIAL_AUTH_GITHUB_KEY = '14e88b11ac7e43f47d77'
SOCIAL_AUTH_GITHUB_SECRET = 'db0534c1d6d4abcf89ec945b16f813448d27a0c0'

SOCIAL_AUTH_FACEBOOK_KEY = '1023224041182968'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '912d04c2bfa455c23f0b9e1dffa52bc5'  # App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '323374321153-16h557p0s83vct989u5va0bqnvaveibd.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'dP4Gc-DWdiiu1Y0SKuGNdCRC'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False



PAYPAL_RECEIVER_EMAIL = 'sameerbasha170794@gmail.com'
PAYPAL_TEST = True