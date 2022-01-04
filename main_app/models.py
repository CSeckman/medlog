from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Med(models.Model):
  name = models.CharField('Medicine', max_length=50)
  patient = models.CharField(max_length=50, null=True)
  description = models.TextField(max_length=200)
  total_doses = models.IntegerField(blank=True, null=True)
  dose = models.CharField(max_length=100)
  other_details = models.CharField(max_length=150)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("med_detail", kwargs={"med_id": self.id})
  

class Log(models.Model):
  date = models.DateField('Date Given')
  time = models.TimeField() 
  dose_given = models.CharField(max_length=100)
  administered_by = models.CharField(max_length=50)
  
  med = models.ForeignKey(Med, on_delete=models.CASCADE)
  def __str__(self):
      return f"{self.dose_given} given on {self.date}"
    
  class Meta:
    ordering = ['-date']