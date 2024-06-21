from django.shortcuts import render
import requests
from robot.models import Robot
from activity.models import Activity
# Create your views here.
def homePage(request):
    return render(request, 'home.html')

def ottosPage(request):
    robots = Robot.objects.all()


    context = {'robots': robots}
    return render(request, 'ottos.html', context)

def activityListPage(request,robot_id):
    # get robot's activities
    robot_activities = Activity.objects.filter(robot_id=robot_id)
    # get robot

    robot = Robot.objects.get_or_create(robot_id=robot_id)

    context = {'robot_activities': robot_activities, 'robot': robot}
    return render(request, 'activityList.html', context)