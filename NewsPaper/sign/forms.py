from django.contrib.auth.forms import UsernameField
from django.forms import CharField, PasswordInput, TextInput, BooleanField
from typing import Any
from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth.models import Group


class FormMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        add extra attributes to all widgets
        """
        #self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            _class = field.widget.attrs.get('class', '')
            extra = ' form-control'
            if field.widget.input_type == 'checkbox':
                extra = ''
            field.widget.attrs.update({'class': _class + extra,
                                       'placeholder': f'...'})


class CustomSignupForm(FormMixin, SignupForm):
    first_name = CharField()
    last_name = CharField()

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user


class CustomLoginForm(FormMixin, LoginForm):
    pass
