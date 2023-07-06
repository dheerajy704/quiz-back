from .models import Category, Quizzes, Question
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class QuizListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quizzes
        fields=['id','title']

class QuizSerializer(serializers.ModelSerializer):
    # items = serializers.RelatedField(many=True)
    class Meta:
        depth = 1
        model=Question
        fields=['title', 'difficulty', 'answer']