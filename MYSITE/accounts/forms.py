from django import forms

from django.contrib.auth.models import User


from .models import Profile

# BEGIN SignUp
class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            'username', 
            'email',
        ]
        email = {
            'required': True
        }


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    # Добавляем класс к HTML формы
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
            
        self.fields['email'].required = True
# END SignUp



# BEGIN Login
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя'
    )
    password = forms.CharField(
        label='Пароль', 
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'

            self.fields['username'].widget.attrs.update(
                {
                    'placeholder': 'Логин',
                    'aria-label': 'Username',
                    'aria-describedby' : 'addon-wrapping',
                },
            )

            self.fields['password'].widget.attrs.update(
                {
                    'placeholder': 'Пароль',
                },
            )
# END Login



# BEGIN Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image', 
        ]
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
# END Profile



# BEGIN ProfileEmailConfirmForm
class ProfileEmailConfirmForm(forms.Form):
    email_token = forms.CharField(
        label='Код подтверждения',
    )
    
    def __init__(self, *args, **kwargs):
        super(ProfileEmailConfirmForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
# END ProfileEmailConfirmForm



# BEGIN MassEmail
class MassEmailForm(forms.Form):
    title = forms.CharField(
        label='Заголовок',
    )
    text = forms.CharField(
        label='Текст',
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(MassEmailForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
# END MassEmail

