from rest_framework import serializers
from .models import Jobposting


class JobpostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobposting
        fields = '__all__'
