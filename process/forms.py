from django import forms
from .models import Candidate,Attempts

class DateInput(forms.DateInput):
    input_type = 'date'

class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('name', 'date', 'college', 'degree', 'contact_no')
        widgets = {
        	'date': DateInput(),
        }

class CandidateRating(forms.ModelForm):

    class Meta:
        model = Attempts
        fields = ('candidate', 'question', 'ratings')