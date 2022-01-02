from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .models import Med

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def med_index(request):
  meds = Med.objects.all()
  return render(request, 'meds/index.html', {"meds": meds})