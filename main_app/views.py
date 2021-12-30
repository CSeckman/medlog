from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse('Welcome to Med Log')

def about(request):
  return render(request, 'about.html')