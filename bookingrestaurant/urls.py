"""
URL configuration for bookingrestaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from blog.views import (
    home_view,
    menu_view,
    booking_view,
    booking_list_view,
    cancel_booking_view,
    edit_booking_view,
)


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('menu/', menu_view, name='menu'),
    path('booking/', booking_view, name='booking'),
    path('bookings/', booking_list_view, name='booking_list'),
    path('cancel/<int:booking_id>/', cancel_booking_view, name='cancel_booking'),
    path('edit/<int:booking_id>/', edit_booking_view, name='edit_booking'),
]