from django.http import HttpResponse
from django.shortcuts import render
from .models import Exam

def index(request):
    return render(request, 'test_one/index.html')


def profile(request):
    return render(request, 'test_one/profile.html')

def test_study(request):
    e_test = Exam.objects.all()

    trash = {
        'e_test': e_test,
    }


    return render(request, 'test_one/test_study.html', {'trash': trash})
