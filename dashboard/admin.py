from django.contrib import admin

from .models import Chamber, Inward, Dispatch

from django.contrib.auth.models import Group

admin.site.site_header = 'Inventory Dashboard'


class InwardAdmin(admin.ModelAdmin):
     list_display = ('name', 'category', 'quantity',)
     list_filter = ['category']

class ChamberAdmin(admin.ModelAdmin):
     list_display = ('inward','category',)  

class DispatchAdmin(admin.ModelAdmin):
     list_display = ('inward','date',)
     list_filter = ['date']

# Register your models here.
admin.site.register(Inward,InwardAdmin)
admin.site.register(Dispatch,DispatchAdmin)
admin.site.register(Chamber,ChamberAdmin)
#admin.site.unregister(Group)
