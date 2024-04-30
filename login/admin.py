from django.contrib import admin
from .models import voter  # Updated import


@admin.register(voter)  # Updated model reference
class VoterAdmin(admin.ModelAdmin):
    list_display = ["mobile_number", "email"]
