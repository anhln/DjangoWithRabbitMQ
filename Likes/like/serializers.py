from rest_framework import serializers
from .models import *


class QuoteSerializer(serializers.Serializer):
    class Meta:
        model = Quote
        fields = '__all__'
        

class QuoteUserSerializer(serializers.Serializer):
    class Meta:
        model = QuoteUser
        fields = '__all__'
