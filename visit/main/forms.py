from django import forms
from models import Meetings


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meetings

        fields = ['name', 'fullname', 'email', 'nutritionist']
        widgets = {

            'name': forms.TextInput(
                attrs={'id': 'meeting-name', 'required': True, 'placeholder': 'Say something...'}
            ),
            'fullname': forms.TextInput(
                attrs={'id': 'meeting-fullname', 'required': True, 'placeholder': 'Say something...'}
            ),
            'email': forms.EmailInput(
                attrs={'id': 'meeting-email', 'required': True, 'placeholder': 'Say something...'}
            ),
            'nutritionist': forms.TextInput(
                attrs={'id': 'meeting-nutritionist', 'required': True, 'placeholder': 'Say something...'}
            )
        }