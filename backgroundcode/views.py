from django.shortcuts import render
from django.http import HttpResponse
#
#
#
def test(request):
    return HttpResponse("Hello, System!")
def home(request):
    return HttpResponse("Welcome to the Home Page")