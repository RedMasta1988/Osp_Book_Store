from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    return render(request,"1.html")
def index2(request):
    return render(request,"2.html")
def index3(request):
    return render(request,"3.html")
def xxx(request):
    return render(request,"xxx.html")