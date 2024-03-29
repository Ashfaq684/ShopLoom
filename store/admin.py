from django.contrib import admin
from . models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails

# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'category', 'stock', 'created_date', 'modified_date', 'is_available']
    
    prepopulated_fields = {'slug' : ('product_name',)}
    inlines = [ProductGalleryInline]


class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'is_active']
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category')


class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('product__name', 'user__username', 'subject', 'review')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(ProductGallery)