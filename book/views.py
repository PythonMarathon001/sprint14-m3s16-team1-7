from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random

# Create your views here.
def show_books(request):
    allBooks = Book.objects.all()
    randomBooks = Book.objects.all().order_by('?')[:3]
    context = {"allBooks": randomBooks}
    return render(request, 'index.html', context)