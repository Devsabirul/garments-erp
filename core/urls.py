from django.urls import path
from .views import *
urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('add-attandents',addAttandents,name="add_attandents"),
    path('attandents-report',attandentsReport,name="attandents_Report"),
    path('view-attandents-report',viewattandentsreport,name="view_attandents_Report"),
]
