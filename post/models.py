from django.db import models

# Create your models here.

class PostModel(models.Model):
    class Meta:
        db_table = "post"
    # author = models.ForeignKey(UserModel, ondelete=models.CASCADE) 유저모델이 없어서 일단 이렇게 주석처리 합니다
    image_file = models.ImageField(null=False, default=None, upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


