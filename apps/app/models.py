from django.db import models

from django.conf import settings 
from django.contrib.auth.models import User
import logging
from django.core.exceptions import (
    ValidationError,
)

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

    MAX_AGE = 27

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
        return f'Студент {self.account.full_name} Группа:{self.group.name}'


    def save(
        self,
        *args: tuple,
        **kwargs: dict
    ) -> None:
        if self.age > self.MAX_AGE:
            #self.age = self.MAX_AGE
            raise ValidationError(
                f'Допустимый возраст:{self.MAX_AGE}'
                )

        super().save(*args, **kwargs)
    


    class Meta:

        ordering = (
            'account',
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Professor(models.Model):
    FULL_NAME_MAX_LENGTH = 20
    TOPIC_MAX_LENGTH = 30

    TOPIC_JAVA = 'java'
    TOPIC_PYTHON = 'python'
    TOPIC_TS = 'typescript'
    TOPIC_JS = 'javascript'
    TOPIC_RUBY = 'ruby'
    TOPIC_GO = 'golang'
    TOPIC_SQL = 'sql'
    TOPIC_SWIFT = 'swift'
    TOPIC_PHP = 'php'
    TOPIC_DELTHI = 'delphi'
    TOPIC_PERL = 'perl'

    TOPIC_CHOICES = (
        (TOPIC_JAVA, 'Java'),
        (TOPIC_PYTHON, 'Python'),
        (TOPIC_TS, 'Typescript'),
        (TOPIC_JS, 'JavaScript'),
        (TOPIC_RUBY, 'Ruby'),
        (TOPIC_GO, 'Golang'),
        (TOPIC_SQL, 'SQL'),
        (TOPIC_SWIFT, 'Swift'),
        (TOPIC_PHP, 'PHP'),
        (TOPIC_DELTHI, 'Delphi'),
        (TOPIC_PERL, 'Perl'),   
    )

    full_name = models.CharField(
        verbose_name='Полное имя',
        max_length=FULL_NAME_MAX_LENGTH
    
    )
    topic = models.CharField(
        verbose_name='Предмет',
        choices=TOPIC_CHOICES,
        default=TOPIC_JAVA,
        max_length=TOPIC_MAX_LENGTH
    )

    students = models.ManyToManyField(
        'Student'
    )
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ('full_name',)

    def save(self,args,**kwargs) -> None:
        super().save(args,**kwargs)

    def str(self) -> str:
        return f'Teacher: {self.full_name}, teaches: {self.topic}'
