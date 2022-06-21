from rest_framework import serializers
from .models import Jobposting


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobposting
        fields = '__all__'
