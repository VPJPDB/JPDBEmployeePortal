from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class HRReportForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the description here...'}), required=True)
    date = forms.DateField(widget=forms.SelectDateWidget, required=True)

class SafetySurveyForm(forms.Form):
    question_1 = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your response...'}))
    question_2 = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your response...'}))
    question_3 = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your response...'}))

class CheckInForm(forms.Form):
    employee_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter employee name...'}))
    check_in_date = forms.DateField(widget=forms.SelectDateWidget, required=True)
    comments = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter any comments...'}), required=False)

class TrainingFollowUpForm(forms.Form):
    training_module = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter training module...'}))
    completion_date = forms.DateField(widget=forms.SelectDateWidget, required=True)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your feedback...'}), required=False)
