from django.shortcuts import render
import requests

from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.response import Response

from like.serializers import QuoteSerializer, QuoteUserSerializer
from .models import *




class QuoteViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = QuoteSerializer
    # print('im here')
    queryset = Quote.objects.all()
    
    def list(self, request):
        products = Quote.objects.all()
        serializer = QuoteSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class QuoteUserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = QuoteUserSerializer
    queryset = QuoteUser.objects.all()
    
