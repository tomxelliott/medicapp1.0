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
        widgets = {'password': forms.PasswordInput(), }


class UserProfileForm(forms.Form):
    dob = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))

    class Meta:
        model = UserProfile
        fields = ["dob"]

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields["dob"] = forms.DateField()


class EditUserProfileForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ["dob"]

    def __init__(self):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)
        self.fields["dob"] = forms.DateField()