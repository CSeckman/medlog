from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

from .models import Med
from .forms import LogForm

class Home(LoginView):
  template_name = 'home.html'

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
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)