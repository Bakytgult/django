from django.db import models

from django.conf import settings 
from django.contrib.auth.models import User

# class User(models.Model):
#     pass
class Account(models.Model):

    ACCOUNT_FULL_NAME_MAX_LENGTH = 20

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
        max_length=ACCOUNT_FULL_NAME_MAX_LENGTH
    )
    description = models.TextField()

    def __str__(self) -> str:
        return f'Аккаунт:{self.user.id}/{self.full_name}'

    class Meta:

        ordering = (
            'full_name',
        )
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


class Group(models.Model):

    CROUP_MAX_LENGTH = 10

    name = models.CharField(
        max_length=CROUP_MAX_LENGTH
    )

    def __str__(self) -> str:
        return f'Группа:{self.name}'

    class Meta:

        ordering = (
            'name',
        )
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Student(models.Model):

    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE
    )
    age = models.IntegerField(
        'Возраст студента'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT
    )
    gpa = models.FloatField(
        'Средний балл'
    )

    def __str__(self) -> str:
        return f'Аккунт:{self.account}',
        f'Группа:{self.group.name}',
        f'Возраст:{self.age}',
        f'GPA:{self.gpa}'

    class Meta:

        ordering = (
            'account',
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'