from django.db.models.signals import post_save
from .models import CustomUser
from .models import CustomUserAPIKey
from django.dispatch import receiver
from rest_framework_api_key.models import APIKey


@receiver(post_save,sender=CustomUser)
def create_apikey(sender,instance,created,**kwargs):
    if created:
        c,_ = CustomUserAPIKey.objects.create_key(name=instance.username)
        c.user_key = instance
        c.save()
        # api_key.save()
    else:
        instance.apikey.save()

# @receiver(post_save,sender=CustomUser)
# def save_apikey(sender,instance,**kwargs):
    