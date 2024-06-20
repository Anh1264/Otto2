from django.db import models
from robot.models import Robot
# Create your models here.
class Picture(models.Model):
    picture_id = models.AutoField(primary_key= True) 
    robot_id = models.ForeignKey(Robot, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=True, blank=True)
    file_name = models.CharField(max_length=200,null=True, blank=False)
    file_data = models.TextField(null=True, blank = False)
    inf_result = models.IntegerField(null=True, blank=True)
    inf_conf = models.IntegerField(null=True, blank=True)
    cap_time = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False, blank=True)
    inference_ms = models.DurationField(default=0, blank=True)

    def __str__(self):
        return self.file_name