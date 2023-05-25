from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.





class auction_topic(models.Model):
    auction_topic_id = models.AutoField(primary_key=True)
    title_auction_topic = models.CharField(max_length=100) 
    create_date_auction_topic = models.DateField(auto_now=True)

class test(models.Model):
    name = models.CharField(max_length=10)
