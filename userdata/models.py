from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_api_key.models import APIKey,AbstractAPIKey
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.BigIntegerField(max_length=11,unique=True,null=True)

    # def save(self,*args,**kwargs):
    #     key = CustomUserAPIKey.objects.create_key(name = self.first_name)
    #     key.save()
    #     super(CustomUser, self).save(*args, **kwargs)


class CustomUserAPIKey(AbstractAPIKey):
    user_key = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='apikey',null=True,blank=True)