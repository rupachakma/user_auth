from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class myAdmin(UserAdmin):
    list_display = ("username", "user_type")

admin.site.register(customuser,myAdmin)
