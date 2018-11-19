"""UserAdmin classes"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Models
from users.models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    # Muestra como es el listado en el admin
    list_display = ('pk', 'user', 'phone_number', 'website', 'biography')
    # Para hacer algunos campos clikeables
    list_display_links = ('pk', 'user')
    # Para colocar cuales campos se pueden editar en línea no puede estar también en el de links
    list_editable = ('website', 'phone_number')
    # Para que exista un input de búsqueda en el listado y se filtre por los campos dados
    search_fields = ('user__email', 'user__first_name')
    # Para tener un panel lateral de filtros predeterminados según los campos dados
    list_filter = ('created_at', 'updated_at')

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture')
            )
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (
                ('created_at', 'updated_at'),
            )
        })
    )

    readonly_fields = ('created_at', 'updated_at')

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for user"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
