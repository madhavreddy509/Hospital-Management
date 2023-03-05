from django.contrib import admin
from .models import User,Blog,Appointment

# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Appointment)