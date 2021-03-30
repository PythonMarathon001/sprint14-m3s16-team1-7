from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_users, name='all_users'),
    path('<int:id>/', views.show_user_by_id, name='user_by_id'),
    path('create_user', views.create_user, name='create_user'),
]