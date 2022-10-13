from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, CharField



user = get_user_model()

class UserCreationForm(UserCreationForm):
    """Form class for registraton user"""
    class Meta(UserCreationForm.Meta):
        model = user
        fields = ('email','img','first_name','last_name',)
        exclude = ['username',]

