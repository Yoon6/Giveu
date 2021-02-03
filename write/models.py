from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200) # 작성자 
    title = models.CharField(max_length=200) # 제목
    bodyText = models.TextField() # 내용
    productType = models.CharField(max_length=200) # 후원 물품 유형
    productNum = models.IntegerField() # 목표 개수
    email = models.CharField(max_length=200) # 이메일
    address = models.CharField(max_length=200) # 목적지 주소
    picture = models.ImageField(upload_to='images/write/') # 사진

    def __str__(self):
        return self.title