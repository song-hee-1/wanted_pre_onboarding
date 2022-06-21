from django.db import models


# Create your models here.
class Company(models.Model):
    id = models.BigAutoField(primary_key=True)  # 회사 id
    name = models.CharField(max_length=20)  # 회사명
    password = models.CharField(max_length=20)  # 회사 password
    country = models.CharField(max_length=20)  # 국가
    region = models.CharField(max_length=20)  # 지역

    class Meta:
        db_table = 'company'
