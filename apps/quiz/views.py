from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models
import django_filters.rest_framework
from .serializers import CategorySerializer, QuizListSerializer, QuizSerializer
from apps.users.mixins import CustomLoginRequiredMixin

# Create your views here.


class categoryList( ListAPIView):
    queryset= models.Category.objects.all()
    serializer_class= CategorySerializer

class QuizList( ListAPIView):
    queryset= models.Quizzes.objects.all()
    serializer_class= QuizListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category']


class Quiz( ListAPIView):
    queryset= models.Question.objects.all()
    serializer_class= QuizSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['quiz']
    