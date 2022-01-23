from django.http import HttpResponse
from django.shortcuts import render
from .models import Exam, TestingWithChangeAnswer
from .forms import ExamForm, TestWChA

def index(request):
    return render(request, 'test_one/index.html')


def profile(request):
    return render(request, 'test_one/profile.html')

def test_study(request):
    e_test = Exam.objects.all()
    e_test_v2 = TestingWithChangeAnswer.objects.all()
    trash = {
        'e_test': e_test,
        'e_test_v2': e_test_v2
    }

    return render(request, 'test_one/test_study.html', {'trash': trash})

def add_test(request):
    form_old = ExamForm()
    form = TestWChA()
    trash = {
        'form': form,

    }
    return render(request, 'test_one/add_test.html', {'trash': trash})