from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _


class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(max_length=254, label=_("E-mail"))

    def clean(self):
        email = self.cleaned_data.get('email')
        return self.cleaned_data

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     email = self.cleaned_data.get('email')

    #     # if username and password:
    #     if email and password:
    #         # self.user_cache = authenticate(username=username,
    #                                        # password=password)
    #         print 'DEBUG: ', email
    #         self.user_cache = authenticate(email=email,
    #                                        password=password)
    #         print "User is active", self.user_cache.is_active
    #         if self.user_cache is None:
    #             raise forms.ValidationError(
    #                 self.error_messages['invalid_login'],
    #                 code='invalid_login',
    #                 params={'username': self.username_field.verbose_name},
    #             )
    #         elif not self.user_cache.is_active:
    #             raise forms.ValidationError(
    #                 self.error_messages['inactive'],
    #                 code='inactive',
    #             )
    #     print self.get_user()
    #     return self.cleaned_data
