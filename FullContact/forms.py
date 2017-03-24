from django import forms
from django.contrib.auth.models import User

class GetEmail(forms.Form):
	email = forms.EmailField()