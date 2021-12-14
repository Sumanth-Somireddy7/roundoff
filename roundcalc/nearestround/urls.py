from django.urls import path
from . import views

urlpatterns = [
    path('roundoff/',views.roundoff,name='roundoff')
]