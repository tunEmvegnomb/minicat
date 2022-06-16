from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
     
      username = models.CharField(max_length=10, unique=True)
      password = models.CharField(max_length=200)
      email = models.EmailField(max_length=100)
      created_date = models.DateField(auto_now_add=True)
  
      def __str__(self):
          return self.username
    
    
    