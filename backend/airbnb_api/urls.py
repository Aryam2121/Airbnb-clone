from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.get_listings),
    path('add_listing/', views.add_listing),
]