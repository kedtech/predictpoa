from django.contrib import admin
from . models import Ticket, FreeTipsGame, vipTipsGame, RollTipsGame
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_state')
    list_select_related = ('profile', )

    def get_state(self, instance):
        return instance.profile.state
    get_state.short_description = 'State'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.site_header = 'Palsbet Admin Panel'
admin.site.site_title = 'Palsbet Admin Panel'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Ticket)
admin.site.register(FreeTipsGame)
admin.site.register(vipTipsGame)
admin.site.register(RollTipsGame)
