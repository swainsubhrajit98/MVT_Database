from django.contrib import admin

# Register your models here.
from App.models import *

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecords)
