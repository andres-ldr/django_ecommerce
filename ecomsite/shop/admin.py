from django.contrib import admin

from .models import Order, Product

# Register your models here.

admin.site.site_header = "E-commerce site Admin"
admin.site.site_title = "E-commerce site Admin Area"
admin.site.index_title = "Welcome to E-commerce site Admin Area"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    list_display = (
        "title",
        "price",
        "discount_price",
        "category",
        "description",
        "image",
    )
    search_fields = ("title", "category")
    list_filter = ["category"]
    # fields
    fields = ("title", "price")
    # Actions
    actions = ["change_category_to_default"]
    change_category_to_default.short_description = "Change category to default"
    # editable fields
    list_editable = ("price", "category")


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
