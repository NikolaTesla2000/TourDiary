from django.contrib import admin
from .models import Description
from .models import Contact
# Register your models here.
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Description,DescriptionAdmin)
admin.site.register(Contact)
