from django.contrib import admin

from .models import Filme

class FilmeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}

admin.site.register(Filme, FilmeAdmin)

# Register your models here.
