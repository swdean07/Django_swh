from django.db import models

# Create your models here.
class Sports(models.Model):
    title = models.CharField("스포츠 종목", max_length=100)
    content = models.TextField("스포츠 내용")
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜 자동 저장

    def __str__(self):
        return self.title