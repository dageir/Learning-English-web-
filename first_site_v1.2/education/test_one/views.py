from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    return HttpResponse('<h1>Тестовая страница.</h1>')


def cats(request):
    return HttpResponse('<h1>Категории тестовой страницы.</h1>')

