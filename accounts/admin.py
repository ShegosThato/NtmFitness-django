from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MemberCreationForm, MemberChangeForm
from .models import Member


class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
    list_display = ['email', 'first_name', 'last_name', 'id_num']
    model = Member


admin.site.register(Member, MemberAdmin)
