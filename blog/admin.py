from django.contrib import admin
from .models import Post, Comment, PostGallery, Image, PostProducts, BookAParty
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


class GalleryImageInline(admin.TabularInline):
    model = PostGallery.images.through

class ProductImageInline(admin.TabularInline):
    model = PostProducts.images.through

@admin.register(PostGallery)
class GalleryImageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'title_image')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GalleryImageInline]
    summernote_fields = ('description',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'title_image', 'description')
        }),
    )

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')

@admin.register(PostProducts)
class ProductsImageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'title_image')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]
    summernote_fields = ('description', 'excerpt')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'title_image', 'description', 'excerpt')
        }),
    )


@admin.register(BookAParty)
class BookAPartyAdmin(admin.ModelAdmin):
    list_display = ('party_theme', 'number_of_teepees', 'city', 'date', 'approved')
    list_filter = ('approved', 'party_theme', 'date')
    search_fields = ('city', 'date', 'email', 'phone_number')
    actions = ['approve_party']

    def approve_party(self, request, queryset):
        queryset.update(approved=True)