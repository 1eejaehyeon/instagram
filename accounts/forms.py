from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm

from .models import User
from django import forms

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].requried = True
        self.fields['first_name'].requried = True
        self.fields['last_name'].requried = True



    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 사용중인  이메일입니다.")
            return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name","website_url", "bio", "phone_number", "gender"]



class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password2(self):
        old_password = self.cleaned_data("old_password")
        new