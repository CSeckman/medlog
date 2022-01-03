from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .models import Med
from .forms import LogForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def med_index(request):
  meds = Med.objects.all()
  return render(request, 'meds/index.html', { "meds": meds })

def med_detail(request, med_id):
  med = Med.objects.get(id=med_id)
  log_form = LogForm()
  return render(request, 'meds/details.html', { 'med': med, 'log_form': log_form })


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

def log_dose(request, med_id):
  form = LogForm(request.POST)
  if form.is_valid():
    new_log = form.save(commit=False)
    new_log.med_id = med_id
    new_log.save()
  return redirect('med_detail', med_id=med_id)