from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone', 'organization', 'address')
        
        widgets = {
            'email': forms.TextInput(attrs={'placeholder':'abc123@gmail.com'}), 
            'phone': forms.TextInput(attrs={'placeholder':'ex) +821012345678'}), 
            'organization': forms.TextInput(attrs={'placeholder':'organization', 'disabled':True, 'required':False}),
            'address': forms.TextInput(attrs={'placeholder':'address', 'disabled':True, 'required':False}), 
            'password1': forms.TextInput(attrs={'placeholder':'password'}),  
            'password2': forms.TextInput(attrs={'placeholder':'confirm password'}), 
        }
        labels = {
            'email': 'Email',
            'phone': 'Phone Number',
            'organization': 'Organization',
            'address': 'Organization Address',
            'password1': 'Password',
            'password1': 'Comfirm Password',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['organization'].required = False
        self.fields['address'].required = False


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'organization', 'address',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]