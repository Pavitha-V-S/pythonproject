#from django.contrib import admin
#from .models import District, Branch

#admin.site.register(District)
#admin.site.register(Branch)
from django.contrib import admin
from .models import District, Branch

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name','wikipedia_link',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'district','sub_areas',)
    list_filter = ('district',)
