from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomChangeForm,CustomCreationForm
from .models import CustomUser , websites
# Register your models here.

class CustomAdmin(UserAdmin):
    add_form=CustomCreationForm
    form=CustomChangeForm
    model=CustomUser
    list_display=('email','is_staff','is_active')
    list_filter=('email','is_staff','is_active')
    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Permissions',{'fields':('is_staff','is_active')}))

    add_fieldsets=[
        (None,{'classes':('wide',),
        'fields':('email','name','password','phone','secondPhone','is_staff','is_active','secondEmail','address','question','answer')
        })
    ]

    search_fields=('email',)
    ordering=('email',)

admin.site.register(CustomUser,CustomAdmin)
admin.site.register(websites)
