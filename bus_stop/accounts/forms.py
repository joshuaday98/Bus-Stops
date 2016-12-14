from django import forms
from .models import Member


class MemberRegistrationForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ('dob',
                  'email',
                  'first_name',
                  'last_name',
                  'gender',)
