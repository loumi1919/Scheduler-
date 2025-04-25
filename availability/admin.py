from django.contrib import admin

from availability.models import Availability


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["date", "start", "end", "status"]



admin.site.register(Availability, AuthorAdmin)