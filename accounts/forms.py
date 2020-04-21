from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Member


class MemberCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ('email', 'username', 'first_name', 'last_name', 'id_num')


class MemberChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = Member
        fields = UserChangeForm.Meta.fields
