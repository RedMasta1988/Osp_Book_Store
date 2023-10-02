from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

def shop (request):
    book = Book.objects.all()
    context = {
        'pr' : book
    }
    return render (request,'shop.html', context)