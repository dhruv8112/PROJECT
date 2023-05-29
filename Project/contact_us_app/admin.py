from django.contrib import admin

# Register your models here.
from .models import contact

class contactRegister(admin.ModelAdmin):
    list_display=['name','Email','contact_no','subject','message',]
    
    
admin.site.register(contact, contactRegister)
