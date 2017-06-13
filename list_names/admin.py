from django.contrib import admin

from .models import ListNames

class NameModel(admin.ModelAdmin):
    list_display = ["name", "timestamp"]
    list_display_links = ["timestamp"]
    list_editable = ["name"]
    list_filter = ["timestamp"]
    search_fields = ["name"]

    class Meta:
        model = ListNames


admin.site.register(ListNames, NameModel)
