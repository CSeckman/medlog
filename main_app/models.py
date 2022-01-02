from django.db import models

# Create your models here.
class Med(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=200)
  total = models.IntegerField(blank=True, null=True)
  dose = models.CharField(max_length=100)
  other_details = models.CharField(max_length=150)
  
  def __str__(self):
    return self.name