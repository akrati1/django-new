from django.shortcuts import render
from user.models import Post
from .serializer import Postserializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = Postserializer
