from django.contrib import admin
from django.urls import path
from api.views import *


urlpatterns = [
    path('auth/', profile.AuthView.as_view()),
    path('profile/<int:id>/', profile.ProfilePageView.as_view()),
]
