from django.contrib import admin
from flatblocks.models import FlatBlock
from flatblocks.settings import ADMIN_SHOW_ALL_SITES_BLOCKS


if ADMIN_SHOW_ALL_SITES_BLOCKS:
    list_filter = ['site', ]
else:
    list_filter = []


class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['slug', ]
    list_display = ('slug', 'header', 'content', 'site')
    search_fields = ('slug', 'header', 'content')
    list_filter = list_filter

    def queryset(self, request):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.

        Copied from Django ModelAdmin with minimal changes 
        """
        if ADMIN_SHOW_ALL_SITES_BLOCKS:
            qs = self.model.all_objects.get_query_set()
        else:
            qs = self.model._default_manager.get_query_set()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.ordering or () # otherwise we might try to *None, which is bad ;)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

admin.site.register(FlatBlock, FlatBlockAdmin)
