from django.contrib import admin

from .models import Ni, Job


@admin.register(Ni)
class NiModelAdmin(admin.ModelAdmin):
    list_display = ('text', 'user_id', 'chat_id')


@admin.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'chat_id', 'status', 'target')
