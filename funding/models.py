from django.db import models

from user.models import User

# Create your models here.

class Funding(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE) # 올린 유저 이름
    # name = models.CharField(max_length=50) # 올린 유저 이름
    title = models.CharField(max_length=200) # 펀딩 이름
    bodyText = models.TextField() # 펀딩 글 상세내용
    created_at = models.DateField(auto_now=True) # 펀딩 글 작성 시간
    product_type = models.CharField(max_length=50) # 제품 유형
    product_num = models.IntegerField(default=0) # 제품 목표 개수
    email = models.CharField(max_length=200) # 이메일
    address = models.CharField(max_length=500) # 최종 목적지
    photo = models.ImageField(upload_to='images/fundings/') # 펀딩 글 썸네일
    deadline = models.CharField(max_length=50) # 마감 기한

    community = models.CharField(max_length=100) # 대행업체 이름
    community_address = models.CharField(max_length=500) # 보내야할 주소
    
    current_product_num = models.IntegerField(default=0) # 현재 기부 현황

    user = models.ManyToManyField(User, related_name="user_set", blank=True)

    def __str__(self):
        return self.title
    
    # @property
    def funding_counter(self):
        if self.current_product_num == self.product_num:
            return -1
        self.current_product_num += 1
        self.save()
        return self.current_product_num