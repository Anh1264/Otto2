from django.contrib import admin
from .models import Activity
# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('robot_id', 'on_time', 'off_time', 'active_time', 'scans', 'wifi', 'cam')