from django.contrib import admin
from .models import LogMessage, Thing

# Register your models here.
admin.site.register(LogMessage)
admin.site.register(Thing)