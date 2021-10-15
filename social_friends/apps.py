from django.apps import AppConfig
from django.db.models.signals import pre_save
from .receivers import set_user_code

class SocialFriendsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social_friends'
    pre_save.connect(set_user_code)


    