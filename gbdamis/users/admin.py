from django.contrib import admin
from django.contrib.auth import get_user_model

from .oldforms import (
    UserAdminCreationForm, UserAdminChangeForm,AdminPasswordChangeForm
)

User = get_user_model()

class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
    ('Authentication', {'fields': ('username', 'email','password')}),
    ('Personal info', {'fields': ('first_name', 'other_names', 'date_of_birth', 'phone_number', 'whatsapp_number', 'nationality')}),
    ('Job Details', {'fields': ('company_name','drilling_licence','region_or_zone','field','profession', 'education')}),
    ('Permissions and Verificatiion', {'fields': ('admin', 'active', 'verified', 'is_staff', 'profile_complete')}),
    ('Referee', {'fields': ('referee', 'referee_contact',)}),

    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ( 'username', "password", "password2", 'first_name', 'other_names' ,'admin',),
            },
        ),
    )
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ['username', 'first_name', 'other_names', 'admin' ]
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

admin.site.register(User, CustomUserAdmin)




