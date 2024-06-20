from django.contrib import admin
from .models import Robot
# Register your models here.
class RobotAdmin(admin.ModelAdmin):
    list_display = ('robot_id', 'name', 'type', 'location', 'status')
    search_fields = ('name', 'location', 'type')

admin.site.register(Robot,RobotAdmin)