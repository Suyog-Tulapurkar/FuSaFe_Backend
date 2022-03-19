from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import TreeviewlistSerializer
from .models import Treeviewlist


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is FuSaFe TreeView.")

class TreeviewlistView(viewsets.ModelViewSet):
    serializer_class = TreeviewlistSerializer
    queryset = Treeviewlist.objects.all()