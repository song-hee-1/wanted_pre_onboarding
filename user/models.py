from django.db import models


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=15, primary_key=True) # 로그인 시 사용할 id
    password = models.CharField(max_length=20) # 로그인 시 사용할 password
    name = models.CharField(max_length=15) # 사이트에서 사용할 name
    email = models.EmailField(max_length=50, unique=True) # 사이트에서 사용할 email

    class Meta:
       db_table = 'user'