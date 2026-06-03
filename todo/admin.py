from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'is_completed', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')