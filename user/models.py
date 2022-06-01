from django.db import models
from django.contrib.auth.models import AbstractUser
from configparser import MAX_INTERPOLATION_DEPTH

class UserModel(AbstractUser):
    class Meta:
        db_table = "user"
        
    # username = models.CharField(max_length=20, null=False) 
    # password = models.CharField(max_length=256, null=False)

