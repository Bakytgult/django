from django.db import models
from django.db.models import QuerySet

from django.conf import settings 
from django.contrib.auth.models import User

from django.core.exceptions import (
    ValidationError,
)

from abstracts.models import DateTimeCustom



# class AccountQuerySet(QuerySet):

#     def get_superusers(self) -> QuerySet:
#         return self.filter(
#             user__is_superuser=True
#             )



class Account(DateTimeCustom):
    
    ACCOUNT_FULL_NAME_MAX_LENGTH = 20

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
        max_length=ACCOUNT_FULL_NAME_MAX_LENGTH
    )
    description = models.TextField()
    # objects = AccountQuerySet().as_manager()
    
    def __str__(self) -> str:
        return f'Аккаунт:{self.user.id}/{self.full_name}'

    class Meta:
        ordering = ('full_name',)
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


# class GroupQuerySet(QuerySet):
    
#     HIGH_GPA_LEVEL = 4.0

#     def get_students_with_high_gpa(self) -> QuerySet:
#         return self.filter(
#             )



class Group(DateTimeCustom):

    CROUP_MAX_LENGTH = 10

    name = models.CharField(

        max_length=CROUP_MAX_LENGTH
    )
    # objects = GroupQuerySet().as_manager()
    
    def __str__(self) -> str:
        return f'Группа:{self.name}'

    class Meta:

        ordering = ('name',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'



class StudentQuerySet(QuerySet):

    ADULT_AGE = 18

    def get_adult_students(self) -> QuerySet:
        return self.filter(
            age__gte=self.ADULT_AGE
        )



class Student(DateTimeCustom):

    MAX_AGE = 24

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
    # objects = StudentQuerySet().as_manager()

    def __str__(self) -> str:
        return f'Студент {self.account.full_name} Группа:{self.group.name}'

    def save(self, *args: tuple, **kwargs: dict) -> None:
        if self.age > self.MAX_AGE:
            
            raise ValidationError(
                f'Допустимый возраст: {self.MAX_AGE}'
            )
        super().save(*args, **kwargs)

    def delete(self) -> None:
        datetime_now: self.datetime = self.datetime.now()

        self.datetime_deleted = datetime_now

        self.save(
            update_fields=['datetime_deleted']
        ) 

    class Meta:

        ordering = ('account',)
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'



class Professor(DateTimeCustom):

    FULL_NAME_MAX_LENGTH = 40
    TOPIC_MAX_LENGTH = 30

    TOPIC_JAVA = 'java'
    TOPIC_PYTHON = 'python'
    TOPIC_GOLANG = 'golang'
    TOPIC_TYPESCRIPT = 'typescript'
    TOPIC_SWIFT = 'swift'
    TOPIC_PHP = 'php'
    TOPIC_SQL = 'sql'
    TOPIC_RUBY = 'ruby'

    TOPIC_CHOICES = (
        (TOPIC_JAVA,'Java'),
        (TOPIC_PYTHON,'Python'),
        (TOPIC_GOLANG,'Golang'),
        (TOPIC_TYPESCRIPT,'Typescript'),
        (TOPIC_SWIFT,'Swift'),
        (TOPIC_PHP,'PHP'),
        (TOPIC_SQL,'SQL'),
        (TOPIC_RUBY,'Ruby'),
    )

    full_name = models.CharField(
        verbose_name='полное имя',
        max_length=FULL_NAME_MAX_LENGTH
    )

    topic = models.CharField(
        verbose_name='предмет',
        choices=TOPIC_CHOICES,
        default=TOPIC_JAVA,
        max_length=TOPIC_MAX_LENGTH
    )
    students = models.ManyToManyField(
        'Student'
    )

    def str(self) -> str:
        return f'Преподователь: {self.full_name}, Квалификафии: {self.topic}'

    def save(self, *args: tuple, **kwargs: dict) -> None:
        super().save(*args,**kwargs)

    class Meta:

        ordering = ('full_name',)
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        
