from django.contrib import admin

from blog.models import Post


class AdminPosts(admin.ModelAdmin):
    list_display = ("author", "title", "created_date", "published_date")


admin.site.register(Post, AdminPosts)
