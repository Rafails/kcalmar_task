from django import forms
from models import Meetings


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meetings

        fields = ['name', 'fullname', 'email']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'meeting-name', 'required': True, 'placeholder': 'Say something...'}
            ),
            'fullname': forms.TextInput(
                attrs={'id': 'meeting-fullname', 'required': True, 'placeholder': 'Say something...'}
            ),
            'email': forms.EmailInput(
                attrs={'id': 'meeting-email', 'required': True, 'placeholder': 'Say something...'}
            )
        }