from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class PostInline(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


# Register your models here.
admin.site.register(Post, PostInline)
admin.site.register(Comment)


admin.site.site_header = "NTM Fitness"
admin.site.site_title = "NTM Fitness Portal"
admin.site.index_title = "Welcome to NTM Fitness Club Portal"
