import random
from typing import Any
from datetime import datetime
from django.contrib.auth.hashers import make_password 

from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import (
    User,
)

from app.models import (
    Group,
    Account,
    Student,
    Professor,
)
import names

class Command(BaseCommand):
    """Custom command for filling up database.

    Test data only
    """
    help = 'Custom command for filling up database.'

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        pass

    def _generate_groups(self) -> None:
        """Generate Group objs."""

        def generate_name(inc: int) -> str:
            return f'Группа {inc}'

        inc: int
        for inc in range(20):
            name: str = generate_name(inc)
            Group.objects.create(
                name=name
            )

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()

        self._generate_groups()

        print(
            'Generating Data: {} seconds'.format(
                (datetime.now()-start).total_seconds()
            )
        )

    TOTAL_GENERATE_USERS = 500

    def _generate_users(self) -> None:
        """Generate User objects."""

        _email_patterns: tuple = (
            '@gmail.com', '@outlook.com', '@yahoo.com',
            '@inbox.ru', '@inbox.ua', '@inbox.kz',
            '@yandex.ru', '@yandex.ua', '@yandex.kz',
            '@mail.ru', '@mail.ua', '@mail.kz',
        )

        super_users: int = User.objects.filter(is_superuser="True")

        if super_users.count() <= 1:
            User.objects.create(
                is_superuser = True,
                is_staff = True,
                username = 'putin',
                email = 'vladimir_putin@mail.ru',
                password = 'КрымНаш228',
                first_name = 'Владимир',
                last_name = 'Путин',
            )
        elif super_users.count() >= 2:
            print('Superuser quantity is limited')

        if User.objects.count() <= 2:
            try:
                inc: int
                for inc in range(TOTAL_GENERATE_USERS):
                    user_password: str = 'Qwerty0123456789Qwerty'
                    user_first_name: str = names.get_first_name()
                    user_last_name: str = names.get_last_name()
                    User.objects.create(
                        first_name = user_first_name,
                        last_name = user_last_name,
                        password = make_password(user_password),
                        username = f'{user_firstname.lower()}{user_last_name.lower()}',
                        email = f'{user_first_name.lower()}.{user_last_name.lower()}{random.choice(_email_patterns)}'),
            except Exception:
                print('Users count out of TOTAL_GENERATE_USERS')