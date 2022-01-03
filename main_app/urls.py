from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('meds/', views.med_index, name='med_index'),
  path('meds/<int:med_id>/', views.med_detail, name='med_detail')
]