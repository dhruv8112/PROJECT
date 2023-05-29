from django.contrib import admin

# Register your models here.

from .models import *

class userAdmin(admin.ModelAdmin):
    list_display = ['age','address','contact','last','First','country',]
    
    
admin.site.register(user,userAdmin)