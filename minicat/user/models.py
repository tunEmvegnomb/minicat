from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserModel(models.Model):
    class Meta:
        db_table = "user"
        
    username = models.CharField(max_length=20, null=False) 
    password = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
