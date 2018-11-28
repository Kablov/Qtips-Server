from django.contrib import admin
from django.urls import path
from api.views import *


urlpatterns = [
    path('code/request/', sms_code.RequestCodeView.as_view()),
    path('code/verify/', sms_code.PhoneNumberVerificationView.as_view()),
    path('signup/', profile.SignUpView.as_view()),
    path('profile/<int:id>/', profile.ProfilePageView.as_view()),
    path('profile/me/', profile.OwnProfilePageView.as_view()),
]
