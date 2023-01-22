from django.contrib import admin
from .models import Cards

class CardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cards, CardAdmin)