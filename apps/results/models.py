from email.policy import default
from string import digits
from django.db import models
from apps.users.models import User

# Create your models here.
class Result(models.Model):
    user= models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    quiz_name = models.CharField('quiz name', max_length=200 )
    score = models.IntegerField(
        'score', default= 0
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )