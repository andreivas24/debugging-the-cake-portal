from django import forms
from cake_user.models.user_model import User
from user_profile.models.user_profile_model import Profile


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['_full_name', 'image', 'about_me']
