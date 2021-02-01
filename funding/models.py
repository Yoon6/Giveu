from django.db import models

# Create your models here.

class Funding(models.Model):
    title = models.CharField(max_length=200) # 펀딩 이름
    created_at = models.DateField(auto_now=True) # 펀딩 글 작성 시간
    photo = models.ImageField(upload_to='images/fundings/') # 펀딩 글 썸네일
    description = models.TextField() # 펀딩 글 상세내용
    funding_count = models.IntegerField(default=0) # 펀딩 수

    def __str__(self):
        return self.title
    
    @property
    def funding_counter(self):
        self.funding_count += 1
        self.save()
        return self.funding_count