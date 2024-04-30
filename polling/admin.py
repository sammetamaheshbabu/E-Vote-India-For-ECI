from django.contrib import admin
from .models import Party, Vote

# Register Party and Vote models
admin.site.register(Party)
admin.site.register(Vote)
