from django.urls import path
from . import views
urlpatterns = [
    path('', views.PictureMixinView.as_view()),
    path('create/', views.PictureMixinView.as_view()),
    path('<str:picture_id>/', views.PictureMixinView.as_view()),
    path('<str:picture_id>/update/', views.PictureMixinView.as_view()),
    path('<str:picture_id>/destroy/', views.PictureMixinView.as_view()),
]