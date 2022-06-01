from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = 'user_test'

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)

class FollowModel(models.Model):
    class Meta:
        db_table = 'follow_test'

    followee = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    follower = models.CharField(max_length=20, null=False)