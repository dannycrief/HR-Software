from django.urls import path

from .views import checkTheSame

urlpatterns = [
    path('demo-test/', checkTheSame),
]
