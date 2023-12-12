from django.contrib import admin
from .models import News

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'urlEndpoint')

admin.site.register(News, YourModelAdmin)
