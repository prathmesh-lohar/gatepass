from django.contrib import admin
from .models import userprofile,gatepass,entry

class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'register_number', 'first_name', 'last_name', 'adhar_number', 'mobile_number')
    search_fields = ('user__username', 'first_name', 'last_name', 'adhar_number', 'mobile_number')
    list_filter = ('gender', 'address_distract')

admin.site.register(userprofile, UserProfilesAdmin)


class GatepassAdmin(admin.ModelAdmin):
    list_display = ('gatepass_number', 'user',  'time',  'pass_type', 'master_admin_approval')
    list_filter = ('pass_type', 'master_admin_approval')
    search_fields = ('gatepass_number', 'user__username')

admin.site.register(gatepass, GatepassAdmin)
admin.site.register(entry)

