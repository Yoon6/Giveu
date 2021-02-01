from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bodyText = models.TextField()
    productType = models.CharField(max_length=200)
    productNum = models.IntegerField()

    def __str__(self):
        return self.title