from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUserAPIKey
from rest_framework_api_key.admin import APIKeyModelAdmin
# Register your models here.
CustomUser = get_user_model()
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username','email','first_name','last_name',
    ]


    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Info',{
                'fields':('phone_number',)
            }
        ),  
    )

@admin.register(CustomUserAPIKey)
class CustomUserAPIKeyModelAdmin(APIKeyModelAdmin):
    pass


admin.site.register(CustomUser,CustomUserAdmin)
