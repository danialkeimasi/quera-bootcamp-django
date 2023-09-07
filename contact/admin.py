from django.contrib import admin

from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "message", "created_at", "updated_at", "resolved"]
    list_filter = ["resolved"]
    search_fields = ["name", "email", "phone_number", "message", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    actions = ["mark_as_resolved", "mark_as_unresolved"]

    @admin.display(description="Mark selected as resolved")
    def mark_as_resolved(self, request, queryset):
        queryset.update(resolved=True)

    @admin.display(description="Mark selected as unresolved")
    def mark_as_unresolved(self, request, queryset):
        queryset.update(resolved=False)
