from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_authentications(request):
    return HttpResponse('<h1>Authentication Page</h1>')