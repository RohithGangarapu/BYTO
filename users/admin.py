from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group

class CustomUserAdmin(admin.ModelAdmin):
    exclude = ('user_permissions','groups',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
# Register your models here.
