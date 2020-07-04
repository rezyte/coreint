from django import forms
from django.conf import settings

ACCOUNT_CHOICES = (
    ("A","تایید"),
    ("B", "رد سفارش ")
)

class ConfirmForm(forms.Form):
    confirm_options = forms.ChoiceField(widget=forms.RadioSelect(),choices=ACCOUNT_CHOICES)
