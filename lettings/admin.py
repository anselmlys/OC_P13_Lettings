'''Configure Django admin interfaces for letting and address models.'''

from django.contrib import admin

from lettings.models import Letting, Address


admin.site.register(Letting)
admin.site.register(Address)
