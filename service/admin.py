from django.contrib import admin
from service.models import *

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_number','service_title','service_desc')

# class AboutAdmin(admin.ModelAdmin):
#     list_display=('AboutUs_img', 'AboutUs_small_title', 'AboutUs_title', 'AboutUs_desc',)

admin.site.register(Service,ServiceAdmin)
# admin.site.register(Service,AboutAdmin)