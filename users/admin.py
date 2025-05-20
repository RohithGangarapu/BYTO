from django.contrib import admin
from .models import user
from django.contrib.auth.models import Group

class CustomUserAdmin(admin.ModelAdmin):
    exclude = ('user_permissions','groups',)

admin.site.register(user, CustomUserAdmin)
admin.site.unregister(Group)
# Register your models here.
