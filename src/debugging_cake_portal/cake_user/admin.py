from django.contrib import admin
from cake_user.models.user_model import User, Role

admin.site.register(User)
admin.site.register(Role)
