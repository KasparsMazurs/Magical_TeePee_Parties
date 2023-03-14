from django.contrib import admin
from .models import Post, Comment, PostGallery
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


@admin.register(PostGallery)
class GalleryImageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'title_image')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'title_image', 'description')
        }),
        ('Images', {
            'fields': ('images',),
            'classes': ('collapse',),
        }),
    )
    def get_form(self, request, obj=None, **kwargs):
        self.extra = 3
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['images'].widget = admin.widgets.AdminFileWidget(
            attrs={'multiple': True})
        return form