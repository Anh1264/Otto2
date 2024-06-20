from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.PictureCreateAPIView.as_view()),
]