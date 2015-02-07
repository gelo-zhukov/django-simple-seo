from django.contrib import admin
from django.contrib.contenttypes import generic

from simpleseo.models import SeoMetadata, register_seo_signals


class SeoMetadataInline(generic.GenericStackedInline):
    model = SeoMetadata
    extra = 0
    max_num = 0
    exclude = ('path', 'lang_code', )

    def has_delete_permission(self, request, obj=None):
        return False


class SeoMetadataAdmin(admin.ModelAdmin):
    list_display = ('path', 'lang_code', )
    search_fields = ['path', ]
    list_filter = ('lang_code', )
    exclude = ('content_type', 'object_id', )

    class Media:
        js = (
            'simpleseo/admin.js',
        )


admin.site.register(SeoMetadata, SeoMetadataAdmin)
register_seo_signals()
