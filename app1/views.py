from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bunny(request):
    return HttpResponse('bunny is talented guy')
def meghana(request):
    return HttpResponse('meghana is studying MBBS')
