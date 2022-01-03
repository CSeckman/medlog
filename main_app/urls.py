from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('meds/', views.med_index, name='med_index'),
  path('meds/<int:med_id>/', views.med_detail, name='med_detail'),
  path('meds/create/', views.MedCreate.as_view(), name='meds_create'),
  path('meds/<int:pk>/update/', views.MedUpdate.as_view(), name='med_update'),
  path('meds/<int:pk>/delete/', views.MedDelete.as_view(), name='med_delete'),
  path('meds/<int:med_id>/log_dose', views.log_dose, name='log_dose')
]