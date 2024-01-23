"""Display models in the admin panel."""

from django.contrib import admin

from .models import Product


admin.site.site_header = 'Shopiing list management'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Description of shopping list in the admin panel."""

    list_display = ('name', 'price', 'created_at')
    search_fields = ('name',)
    list_editable = ('price',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'


