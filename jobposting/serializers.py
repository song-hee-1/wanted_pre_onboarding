from rest_framework import serializers
from .models import Jobposting



# 채용공고 전체 목록 조회
class JobpostingSerializer(serializers.ModelSerializer):
    채용공고_id = serializers.IntegerField(source='id')
    회사명 = serializers.CharField(source='company.name')
    국가 = serializers.CharField(source='company.country')
    지역 = serializers.CharField(source='company.region')
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    사용기술 = serializers.CharField(source='skill')


    class Meta:
        model = Jobposting
        fields = ('채용공고_id', '회사명', '국가', '지역', '채용포지션', '채용보상금', '사용기술')


# 채용공고 등록
class JobpostingCreateSerializer(serializers.ModelSerializer):
    회사_id = serializers.IntegerField(source='company_id')
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    채용내용 = serializers.CharField(source='content')
    사용기술 = serializers.CharField(source='skill')

    class Meta:
        model = Jobposting
        fields = ('회사_id', '채용포지션', '채용보상금', '채용내용', '사용기술')

# 채용공고 수정
class JobpostingUpdateSerializer(serializers.ModelSerializer):
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    채용내용 = serializers.CharField(source='content')
    사용기술 = serializers.CharField(source='skill')

    class Meta:
        model = Jobposting
        fields = ('채용포지션', '채용보상금', '채용내용', '사용기술')


# 채용공고 상세정보
class JobPostingDetailSerializer(serializers.ModelSerializer):
    채용공고_id = serializers.IntegerField(source='id')
    회사명 = serializers.CharField(source='company.name')
    국가 = serializers.CharField(source='company.country')
    지역 = serializers.CharField(source='company.region')
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    사용기술 = serializers.CharField(source='skill')
    채용내용 = serializers.CharField(source='content')

    class Meta:
        model = Jobposting
        fields = ('채용공고_id', '회사명', '국가', '지역', '채용포지션', '채용보상금', '사용기술', '채용내용')
