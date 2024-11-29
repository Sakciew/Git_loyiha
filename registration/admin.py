from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import Custom_user_form
from .models import Custom_user_model

class Custom_user_admin(UserAdmin):
    add_form = Custom_user_form
    model = Custom_user_model
    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'address', 'is_staff']

admin.site.register(Custom_user_model, Custom_user_admin)