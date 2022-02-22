
from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from app.models import (
    Account,
    Student,
)



def index(request: WSGIRequest) -> HttpResponse:
    student: Student = Student.objects.first()
    account: Account = student.account
    user: User = account.user
    name: str = user.first_name
    full_name: str = account.full_name
    gpa: float = student.gpa

    text: str = f'<h1>Name: {name}<br> Full name: {full_name}<br> GRA:{gpa}</h1>'

    response: HttpResponse = HttpResponse(text)

    return response

def index_2(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1> Страница: Стартовая </h1>'
    )

def index_3(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = User.objects.all()
    context: dict = {
        'title': 'Главная страница',
        'users': users,
    }
    return render(
        request,
        'index.html',
        context
    )

def show(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'show.html',
        context 
    )

