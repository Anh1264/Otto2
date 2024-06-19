from django.urls import path
from . import views
urlpatterns =[
    path("", views.home_view), #index page -> root page
    path("about/", views.about_view),
    path("hello-world/", views.home_view),
    path("hello-world.html", views.home_view),
]