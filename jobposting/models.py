from django.db import models
from django.utils import timezone


# Create your models here.
class Jobposting(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.ForeignKey('company.Company', on_delete=models.CASCADE)  # 회사
    position = models.CharField(max_length=100)  # 채용포지션
    reward = models.IntegerField()  # 채용보상금
    content = models.TextField()  # 채용내용
    skill = models.CharField(max_length=100)  # 사용기술
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    applys = models.ManyToManyField(
        'user.User', through='Apply', related_name='jobpostings', null=True, blank=True
    )  # 지원 내역을 확인을 위한 테이블

    class Meta:
        db_table = 'jobposting'


class Detail(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.OneToOneField('Jobposting', on_delete=models.CASCADE)

    class Meta:
        db_table = 'detail'


class Apply(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)  # 사용자 id
    jobposting_id = models.ForeignKey('Jobposting', on_delete=models.CASCADE)  # 채용공고 id
    apply_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'apply'
