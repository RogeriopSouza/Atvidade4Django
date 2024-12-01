from rest_framework import serializers
from .models import NotaFiscal 

class NotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = '_all_'