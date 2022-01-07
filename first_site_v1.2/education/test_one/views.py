from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'test_one/index.html')


def profile(request):
    return render(request, 'test_one/profile.html')
