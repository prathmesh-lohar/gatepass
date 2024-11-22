from django.contrib import admin

# Register your models here.
from .models import adminprofile

class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'gender', 'register_number', 'adhar_number')
    search_fields = ('user__username', 'first_name', 'last_name', 'register_number', 'adhar_number')
    list_filter = ('gender', 'type', 'post')
    ordering = ('-register_number',)

    # Optionally, you can customize the form layout
    fieldsets = (
        (None, {
            'fields': ('user', 'register_number', 'first_name', 'last_name', 'gender')
        }),
        ('Address', {
            'fields': ('address_line', 'address_distract', 'address_taluka', 'address_pin_code')
        }),
        ('Contact Info', {
            'fields': ('adhar_number', 'mobile_number', 'photo1', 'photo2')
        }),
        ('Details', {
            'fields': ('type', 'post')
        }),
    )

# Register the AdminProfile model with the AdminProfileAdmin class
admin.site.register(adminprofile, AdminProfileAdmin)