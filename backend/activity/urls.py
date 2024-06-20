from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.ActivityCreateAPIView.as_view()),
    path('', views.ActivityReadAPIView.as_view()),
    path('<int:pk>/', views.ActivityReadAPIView.as_view()),
    path('robot_activities/<int:robot_id>/', views.RobotActivitiesReadAPIView.as_view()),
    path('<int:pk>/update/', views.ActivityUpdateAPIView.as_view()),
    path('<int:pk>/destroy/', views.ActivtyDestroyAPIView.as_view()),
]