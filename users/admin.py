from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class UserAdminConfig(UserAdmin):
    model = CustomUser
    list_filter = ('email', 'username' , 'is_active')
    ordering = ('-created_at',)
    list_display = ('id', 'email', 'username',
                    'is_active', 'is_admin', 'created_at',)
    
    filter_horizontal = ()
    
    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username',  'password1', 'password2', 'is_active', 'is_admin',)}
        ),
    )
    
admin.site.register(CustomUser, UserAdminConfig)