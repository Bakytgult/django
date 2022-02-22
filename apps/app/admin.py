from typing import Optional

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from app.models import (
    Account, 
    Group,
    Student,
    Professor
)


class AccountAdmin(admin.ModelAdmin):
    
    readonly_fields = ()

    # def get_readonly_fields(
    #     self, 
    #     request: WSGIRequest,
    #     obj: Optional[Account] = None
    # ) -> tuple:
    
    #     if not obj:
    #         return self.readonly_fields + ('description',)
    #     return self.readonly_fields


class GroupAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_update',
        'datetime_deleted',
    )

    # def get_readonly_fields(
    #     self, 
    #     request: WSGIRequest,
    #     obj: Optional[Group] = None
    # ) -> tuple:
    
    #     if obj:
    #         return self.readonly_fields + ('name',)
    #     return self.readonly_fields

class StudentAdmin(admin.ModelAdmin):

    readonly_fields = ()
    list_filter = (
        'age',
        'gpa'
    )
    search_fields = (
        'account__full_name',
    )
    list_display = (
        'age',
        'gpa',
    )

    STUDENT_MAX_AGE = 16

    def student_age_validation(
        self,
        obj: Optional[Student]
    ) -> tuple:
        if obj and obj.age <= self.STUDENT_EDIT_MAX_AGE:
            return self.readonly_fields + ('age',)
        return self.readonly_fields

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Student] = None
    ) -> tuple:
        result: tuple = self.student_age_validation(obj)
        return result



class ProfessorAdmin(admin.ModelAdmin):

    readonly_fields = ()



admin.site.register(
    Account, AccountAdmin
)

admin.site.register(
    Group, GroupAdmin
)

admin.site.register(
    Student, StudentAdmin
)

admin.site.register(
    Professor, ProfessorAdmin
)