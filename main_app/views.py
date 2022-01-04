from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

from .models import Med, Log
from .forms import LogForm

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required(login_url='/')
def med_index(request):
  meds = Med.objects.filter(user=request.user)

  return render(request, 'meds/index.html', { "meds": meds })

@login_required(login_url='/')
def med_detail(request, med_id):
  med = Med.objects.get(id=med_id)
  log_form = LogForm()
  logs = Log.objects.filter(med=med_id)
  doses_left = med.total_doses - len(logs)
  return render(request, 'meds/details.html', { 'med': med, 'log_form': log_form, 'doses_left': doses_left})


class MedCreate(LoginRequiredMixin, CreateView):
  login_url = '/'
  model = Med
  fields = ['name', 'patient', 'description', 'total_doses', 'dose', 'other_details'] 
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MedUpdate(LoginRequiredMixin, UpdateView):
  login_url = '/'
  model = Med
  fields = ['description','dose', 'other_details'] 
  

class MedDelete(LoginRequiredMixin, DeleteView):
  login_url = '/'
  model = Med
  success_url = '/meds/'

@login_required(login_url='/')
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
      return redirect('meds_create')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)