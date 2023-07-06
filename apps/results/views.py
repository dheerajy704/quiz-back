from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Result
from .serializers import ResultSerializer
from apps.users.mixins import CustomLoginRequiredMixin
# Create your views here.



class ResultView(CustomLoginRequiredMixin, CreateAPIView):
    queryset = Result.objects.all()
    serializer_class= ResultSerializer

class ResultListView(CustomLoginRequiredMixin, ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


    def get(self, request, *args, **kwargs):
        self.queryset = Result.objects.order_by('-created_at').filter(user=request.login_user)
        return self.list(request, *args, **kwargs)


        