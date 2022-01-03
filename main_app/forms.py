from django.forms import ModelForm
from .models import Log

class LogForm(ModelForm):
  class Meta:
    model = Log
    fields = ['date', 'time', 'dose_given', 'administered_by']