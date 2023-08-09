from django.contrib import admin
from .models import UserProfile, District, Branch

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'district', 'branch', 'account_type')
    list_filter = ('district', 'branch', 'account_type')
    search_fields = ('name', 'email')

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'district')
    list_filter = ('district',)
