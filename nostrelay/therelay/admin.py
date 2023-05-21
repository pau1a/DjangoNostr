from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('type', 'created_at', 'sender', 'event_id', 'pubkey', 'kind', 'tags', 'content', 'sig') 



# Register your models here.
admin.site.register(Event, EventAdmin)