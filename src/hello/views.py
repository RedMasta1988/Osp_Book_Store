from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("This is Sankovich -- Osp_Book_Store")