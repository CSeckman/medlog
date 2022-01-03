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
  return render(request, 'meds/index.html', { "meds": meds })

def med_detail(request, med_id):
  med = Med.objects.get(id=med_id)
  return render(request, 'meds/details.html', { 'med': med })

class MedCreate(CreateView):
  model = Med
  fields = '__all__'
  success_url = '/meds/'
  

class MedUpdate(UpdateView):
  model = Med
  fields = ['description','dose', 'other_details'] 
  

class MedDelete(DeleteView):
  model = Med
  success_url = '/meds/'