from django.contrib import admin
from .models import Problemas

# Register your models here.
class ProblemasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Problemas, ProblemasAdmin)