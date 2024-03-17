from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from users.models import User, EmailVerification
from django import forms
from datetime import timedelta
import uuid
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class UserProfileForm(UserChangeForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True}),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True}),
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "custom-file-input"}), required=False
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "image",
        ]


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя пользователя",
            }
        ),
        label="Имя пользователя",
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя",
            }
        ),
        label="Имя",
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите фамилию",
            }
        ),
        label="Фамилия",
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите email",
            }
        ),
        label="Email",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите пароль",
            }
        ),
        label="Пароль",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите пароль",
            }
        ),
        label="Подтверждение пароля",
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        expiratoin = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(
            code=uuid.uuid4(), user=user, expiratoin=expiratoin
        )
        record.send_verification_email()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя пользователя",
            }
        ),
        label="Имя пользователя",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите пароль",
            }
        ),
        label="Пароль",
    )

    class Meta:
        model = User
        fields = ["username", "password"]
