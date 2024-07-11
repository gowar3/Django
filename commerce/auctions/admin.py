from django.contrib import admin

from .models import Listing, Bid, Comment, Category

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ("creator", "title", "description", "price", "winner", "status")

class BidAdmin(admin.ModelAdmin):
    list_display = ("owner", "listing", "offer")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("poster", "listing", "comment")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "listing")


admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
