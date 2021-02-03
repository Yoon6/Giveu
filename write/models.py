from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bodyText = models.TextField()
    productType = models.CharField(max_length=200)
    productNum = models.IntegerField()
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/write/')


    def __str__(self):
        return self.title