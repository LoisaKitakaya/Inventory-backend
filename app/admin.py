from django.contrib import admin
from .models import Category, Location, InventoryItem

# Register your models here.

class AdminInventoryView(admin.ModelAdmin):

    list_display = [
        'name', 
        'quantity_mass_volume',
        'measurement_in',
        'condition', 
        'last_modified'
    ]

    list_filter = [
        'condition', 
        'category', 
        'location', 
        'archived_on', 
        'last_modified'
    ]

    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(InventoryItem, AdminInventoryView)

admin.site.register(Category)

admin.site.register(Location)