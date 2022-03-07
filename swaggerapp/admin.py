from django.contrib import admin
from .models import *

# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display=['name','stack','proficiency']
    
admin.site.register(Info,InfoAdmin)