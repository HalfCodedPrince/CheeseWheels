from django.contrib import admin

# Register your models here.
from .models import Post, Author, Tag, Site

# Register your models here


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class TagAutoSlug(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag, TagAutoSlug)
admin.site.register(Site)
