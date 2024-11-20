from django.contrib import admin
from .models import Ensemble, Slot, Event

class SlotInline(admin.TabularInline):
    model = Slot
    extra = 1  # Allows adding slots dynamically in the Event admin interface

@admin.register(Ensemble)
class EnsembleAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_slots')  # Display ensemble name and the number of slots

    def num_slots(self, obj):
        return obj.num_slots
    num_slots.admin_order_field = 'num_slots'  # Allows ordering by number of slots


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot_number', 'musician', 'event')

    def musician(self, obj):
        return obj.musician.username if obj.musician else "TBD"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'venue_name', 'ensemble', 'band_name')
    inlines = [SlotInline]  # Add SlotInline here to manage slots for events
