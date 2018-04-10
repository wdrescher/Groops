from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from .models import Profile, Comment


class SignUpForm(ModelForm):
    f_name = forms.CharField()
    l_name = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'f_name', 'l_name', 'password')

class AddComment(ModelForm):
    body = forms.CharField()
    class Meta:
        model = Comment
        fields = ('body',)
