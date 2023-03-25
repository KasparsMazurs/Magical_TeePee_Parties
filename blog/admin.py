from django.contrib import admin
from .models import Post, Comment, PostGallery, Image
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


class ImageInline(admin.TabularInline):
    model = PostGallery.images.through

@admin.register(PostGallery)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'title_image')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'title_image', 'description')
        }),
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')