'''Configure Django admin interfaces for profile model.'''

from django.contrib import admin

from profiles.models import Profile


admin.site.register(Profile)
