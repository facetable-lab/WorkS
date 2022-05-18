from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


# Форма авторизации
class UserLoginForm(forms.Form):
    email = forms.EmailField(label='E-mail адрес', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            user_all = User.objects.filter(email=email)
            if not user_all.exists():
                raise forms.ValidationError('Такого пользователя нет.')
            if not check_password(password, user_all[0].password):
                raise forms.ValidationError('Неверный пароль.')
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Ваш аккаунт отключен.')

        return super(UserLoginForm, self).clean(*args, **kwargs)


# Форма регистрации
class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='E-mail адрес', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return data['password2']
