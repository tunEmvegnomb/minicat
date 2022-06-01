from django.db import models

# Create your models here.

class PostModel(models.Model):
    class Meta:
        db_table = "post"
    # author = models.ForeignKey(UserModel, ondelete=models.CASCADE) 유저모델이 없어서 일단 이렇게 주석처리 합니다
    filename = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
