from django.urls import path
from . import views
urlpatterns=[
    path('', views.homePage, name='home'),
    path('ottos/', views.ottosPage, name='ottos'),
    path('view-activity-list/<int:robot_id>/',  views.activityListPage, name='view-activity-list'),
]