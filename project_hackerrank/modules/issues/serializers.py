from rest_framework import serializers
from .models import Problemas

class ProblemasModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problemas
        fields = ('__all__') 