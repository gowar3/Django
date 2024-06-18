from django.contrib import admin

from .models import Listing, Bid, Comment

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price")

class BidAdmin(admin.ModelAdmin):
    list_display = ("owner", "listing", "offer")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("poster", "listing", "comment")


admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
