from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Med:
  def __init__(self, name, description,  num_of_doses, dose, other_details):
    self.name = name
    self.description = description
    self.num_of_doses = num_of_doses
    self.dose = dose
    self.other_details = other_details

meds = [
  Med('Amoxicilin', 'for ear infection', '20', '5ml, 2 times a day', 'Take with food.'),
  Med('Tylenol', 'to ease booster symptoms',  '10', '5ml, 4 times a day', 'No Details'),
  Med('Incilin', 'Diabetes', '...', '1ml, 3 times a day', 'Inject into thigh'),
]

def med_index(request):
  return render(request, 'meds/index.html', { 'meds': meds })