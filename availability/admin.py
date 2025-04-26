from django.contrib import admin

from availability.models import Event


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["description", "start", "end"]



admin.site.register(Event, AuthorAdmin)

