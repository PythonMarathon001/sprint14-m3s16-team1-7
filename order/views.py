from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_orders(request):
    return HttpResponse('<h1>Orders Page</h1>')