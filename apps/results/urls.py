from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.ResultView.as_view(), name='ResultView' ),
    path('response/',views.ResultListView.as_view(), name='ResultView' ),

]
