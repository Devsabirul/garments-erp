from django.urls import path
from .views import *
urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('add-attandents',addAttandents,name="add_attandents"),
]
