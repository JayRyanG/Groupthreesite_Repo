from django.urls import path
from . import views

urlpatterns = [
    path('gender/list', views.gender_list),
    path('gender/add', views.add_gender)
]