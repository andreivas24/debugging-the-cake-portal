from django.contrib.auth import views as auth_views
from ..forms.login_form import LoginForm


class LoginView(auth_views.LoginView):
    form = LoginForm
    template_name = 'cake_user/login.html'
