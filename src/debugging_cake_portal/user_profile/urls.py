from django.urls import path
from user_profile.views.userprofile_view import profile


app_name = "user_profile"

urlpatterns = [
    path('profile/', profile, name='profile')
]


