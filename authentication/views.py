from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from order.models import Order

# Create your views here.


def show_all_users(request):
    users = CustomUser.objects.all()
    return render(request, 'users.html', {'users': users})


def show_user_by_id(request, id):
    user = CustomUser.objects.get(id=id)
    orders_by_user = Order.objects.filter(user=user)
    return render(request, 'user_by_id.html', {'orders_by_user': orders_by_user, 'user': user})


def create_user(request):
    return render(request, 'create_user.html', {})