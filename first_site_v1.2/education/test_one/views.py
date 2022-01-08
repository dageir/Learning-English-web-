from django.http import HttpResponse
from django.shortcuts import render

data1 = dict(text='it is simple text', text2='one more simple text')


def index(request):

    return render(request, 'test_one/index.html', data1)


def profile(request):
    data2 = {
        'arr': ['title', 15, 'one day', 5185]

    }
    return render(request, 'test_one/profile.html', data1)
