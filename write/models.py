from django.db import models

from user.models import User

# Create your models here.
class Post(models.Model):
    # name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bodyText = models.TextField()
    productType = models.CharField(max_length=200)
    productNum = models.IntegerField()
    email = models.ForeignKey(User, on_delete=models.CASCADE) # 올린 유저 이름
    address = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/write/')


    def __str__(self):
        return self.title