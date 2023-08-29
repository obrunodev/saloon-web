from django.db import models
from django.contrib.auth.models import User

from accounts.choices import CHOICES_PROFILE_TYPE


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_type = models.PositiveIntegerField(choices=CHOICES_PROFILE_TYPE, default=0)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.user.first_name
