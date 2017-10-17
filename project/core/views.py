from django.shortcuts import render
from django.views.generic import ListView

from .models import User


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html', {'user': user})


def user(request, user_name=None):
    user = User.objects.get_by_natural_key(user_name)

    return render(request, 'user.html', {'user': user})
