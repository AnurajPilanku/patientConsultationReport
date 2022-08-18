from django.contrib import admin

# Register your models here.

from .models import Consultation

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Consultation, AuthorAdmin)