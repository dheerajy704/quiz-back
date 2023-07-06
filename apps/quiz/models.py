from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):

    class Meta:
        verbose_name = ("Quiz")
        verbose_name_plural = ("Quizzes")
        ordering = ['id']

    title = models.CharField(
        max_length=255, default=("New Quiz"), verbose_name=("Quiz Title")
    )
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Question(models.Model):

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")
        ordering = ['id']

    SCALE = (
        (0, ('Fundamental')),
        (1, ('Beginner')),
        (2, ('Intermediate')),
        (3, ('Advanced')),
        (4, ('Expert'))
    )

    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255, verbose_name=("Title")
    )
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name=("Difficulty")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=("Date Created")
    )

    def __str__(self):
        return self.title



class Answer(models.Model):
    
    class Meta:
        verbose_name = ("Answer")
        verbose_name_plural = ("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.CASCADE
    )
    answer_text = models.CharField(
        max_length=255, verbose_name=("Answer Text")
    )
    is_right = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.answer_text