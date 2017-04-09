from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Vrach)
admin.site.register(models.Dolzhnost)
admin.site.register(models.People)