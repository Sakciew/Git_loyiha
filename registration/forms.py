from django.contrib.auth.forms import UserCreationForm
from .models import Custom_user_model

class Custom_user_form(UserCreationForm):
    class Meta(UserCreationForm):
        model = Custom_user_model
        fields = UserCreationForm.Meta.fields+('age', 'address')
