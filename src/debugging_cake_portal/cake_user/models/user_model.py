from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    DEV = 1
    COMPO = 2
    MOD = 3
    ROLE_CHOICES = (
        (DEV, 'Developer'),
        (COMPO, 'Compo'),
        (MOD, 'Moderator')
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    email = models.EmailField(_('email'), unique=True)
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.role}: {self.username}"
