from typing import Optional

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from . models import Account
from . models import Group
from . models import Student

class AccountAdmin(admin.ModelAdmin):

    readonly_fields = ()

    def get_readonly_fields(
        self, 
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:

        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields

class GroupAdmin(admin.ModelAdmin):
    
    readonly_fields = (
        'name',
    )

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = (
        'age',
    )


admin.site.register(
    Account, AccountAdmin
)
admin.site.register(
    Group, GroupAdmin
)
admin.site.register(
    Student, StudentAdmin
)