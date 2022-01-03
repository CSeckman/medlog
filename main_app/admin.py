from django.contrib import admin

# Register your models here.
from .models import Med, Log

admin.site.register(Med)
admin.site.register(Log)