from django.urls import path
from . import views
urlpatterns= [
    path('', views.RobotMixinView.as_view()),
    path('create/', views.RobotMixinView.as_view()),
    path('<int:robot_id>/', views.RobotMixinView.as_view()),
    path('<int:robot_id>/update/', views.RobotMixinView.as_view()),
    path('<int:robot_id>/destroy/', views.RobotMixinView.as_view()),
]