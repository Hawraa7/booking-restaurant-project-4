from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking_list_view, name='home'),
]