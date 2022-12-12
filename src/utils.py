from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("predict", views.predict)
    ]