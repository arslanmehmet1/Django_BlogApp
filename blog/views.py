from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Category, Blog
from .serializers import CategorySerializer
class CategoryView(ModelViewSet): #crud
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



