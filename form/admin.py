from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'membership_no', 'state_of_origin', 'lga', 'phone', 'created_at')
    search_fields = ('full_name', 'membership_no', 'state_of_origin', 'lga', 'phone')
    list_filter = ('state_of_origin', 'lga', 'created_at')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        (None, {
            'fields': ('full_name', 'membership_no', 'phone')  # Added phone here
        }),
        ('Details', {
            'fields': ('state_of_origin', 'lga', 'passport_photo')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
    )