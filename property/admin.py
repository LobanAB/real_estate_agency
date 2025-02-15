from django.contrib import admin

from .models import Flat, Complaint
from property.models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'owner', 'address',)
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'has_balcony', 'rooms_number')
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


@admin.register(Flat, Complaint)
class PersonAdmin(admin.ModelAdmin):
    pass
