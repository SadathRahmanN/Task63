from django.contrib import admin
from .models import Destination

# Customizing the display of Destination model in the admin panel
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'weather', 'location', 'google_map_link')  # Customize the columns shown
    search_fields = ('name', 'location')  # Fields to be searchable in admin
    list_filter = ('weather',)  # You can add filters by weather
    ordering = ('name',)  # Default ordering

    # Customizing the form appearance (optional)
    fieldsets = (
        (None, {'fields': ('name', 'weather', 'location', 'google_map_link', 'image', 'description')}),
    )

# Registering the Destination model with the admin interface
admin.site.register(Destination, DestinationAdmin)
