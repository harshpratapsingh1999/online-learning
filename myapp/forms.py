from django import forms
from .models import user_details

class user_details_forms(forms.ModelForm):
    class Meta:
        model = user_details
        exclude = ['user_id']



    