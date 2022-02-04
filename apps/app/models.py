from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#class User(models.Model):
 #   pass



class Account(models.Model):
    ACCOUNT_FULL_NAME_MAX_LENGHT = 20
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )
    full_name = models.CharField(
        max_length = ACCOUNT_FULL_NAME_MAX_LENGHT
    )
    
    description = models.TextField()

    def __str__(self) -> str:
        return f'Account: {self.user.id} / {self.full_name}'

    class Meta:
        ordering = (
            'full_name',
        )
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'



# Create your models here.
