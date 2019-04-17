from django.contrib import admin

from .models import MetaTable, PassedLegislation, all_links, votes
# Register your models here.

admin.site.register(MetaTable)
admin.site.register(PassedLegislation)
admin.site.register(all_links)
admin.site.register(votes)
