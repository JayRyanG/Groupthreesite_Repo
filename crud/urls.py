from django.urls import path
from . import views

urlpatterns = [
    path('gender/add', views.add_gender)
]