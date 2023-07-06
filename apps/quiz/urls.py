from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('apps.quiz.urls')),
    path('category/',views.categoryList.as_view(), name='catList' ),
    path('quizlist/',views.QuizList.as_view(), name='QuizList' ),
    path('quiz/',views.Quiz.as_view(), name='QuizList' )


]
