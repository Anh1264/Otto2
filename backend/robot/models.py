from django.db import models

# Create your models here.
class Robot(models.Model):
    robot_id = models.AutoField(primary_key= True) 
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=False, blank=False) #prototype, deployed
    location = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Model{self.robot_id} -{self.name} at {self.location}"
    