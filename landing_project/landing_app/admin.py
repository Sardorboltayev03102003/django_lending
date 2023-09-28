


from django.contrib import admin

from .models import Customer, Sardor


class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','name','email','message')
    list_filter = ('name','email')
    search_fields = ('name',)

admin.site.register(Customer,CustomerAdmin)
# Register your models here.

@admin.register(Sardor)
class SardorAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism')
