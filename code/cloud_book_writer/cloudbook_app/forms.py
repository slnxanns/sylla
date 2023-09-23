from django import forms
from .models import Document
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file')

##########################################################################################

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        validators=[validate_password],  # Validate the password using Django's built-in validators
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
    )
    is_author = forms.BooleanField(
        label='Are you an Author?',
        required=False,
        initial=False,  # Default to False
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'is_author']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user
