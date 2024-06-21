from django.db import models
from robot.models import Robot
from datetime import timedelta
class Activity(models.Model):
    activity_id = models.AutoField(primary_key= True) 
    robot_id = models.ForeignKey(Robot, on_delete=models.CASCADE)
    on_time = models.DateTimeField()
    off_time = models.DateTimeField()
    active_time = models.DurationField(default=timedelta())
    scans = models.IntegerField(null=False, blank=False, default=0)
    wifi = models.IntegerField(null=False, blank=False, default=0)
    cam = models.IntegerField(null=False, blank=False, default=0)
    
    def __str__(self):
        return f'Activity-{self.activity_id} from {self.robot_id}'
    

    