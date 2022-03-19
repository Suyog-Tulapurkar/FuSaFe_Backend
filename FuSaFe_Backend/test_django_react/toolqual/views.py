from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is FuSaFe toolQual.")

def testindex(request):
    return HttpResponse("this is a tool qual test")

def testyear(request, year):
    return HttpResponse("this is a tool qual test in year 2005")
