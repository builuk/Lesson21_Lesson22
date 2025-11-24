from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)

from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    age = forms.IntegerField(min_value=0, label="Age")
    is_student = forms.BooleanField(required=False, label="Student?")
    level = forms.ChoiceField(choices=[
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ], label="Level")

