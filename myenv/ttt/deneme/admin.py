from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(City)
admin.site.register(School)
admin.site.register(User)