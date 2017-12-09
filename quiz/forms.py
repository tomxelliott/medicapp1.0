from django.forms import ModelForm
from django.db import transaction
from django.db import models
from django.forms import ModelForm, PasswordInput
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django.forms import ValidationError

from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from models import User, UserProfile


class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ["username", "email", "password"]


class UserProfileForm(forms.Form):
        age = forms.IntegerField()

        class Meta:
                model = UserProfile
                fields = ["age"]

        def __init__(self, *args, **kwargs):
                super(UserProfileForm, self).__init__(*args, **kwargs)
                self.fields["age"] = forms.IntegerField(min_value=1, max_value=120)
                self.initial["email"] = 0


class LoginForm(forms.Form):
        userid = forms.CharField(max_length=100)
        password = forms.CharField(widget=PasswordInput())