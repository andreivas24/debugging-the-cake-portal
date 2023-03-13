from django.shortcuts import redirect, render
from django.contrib import messages
from ..forms.register_form import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account has been created! You are now able to log in")
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'cake_user/register.html', {'form': form})
