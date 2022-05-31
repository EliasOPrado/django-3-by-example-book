from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

    # will pre-populate the slug-field with-
    # the name. Interesting.
    prepopulated_fields = {"slug":("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price",
                    "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]

    # will allow to edit values listed.
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug":("name",)}