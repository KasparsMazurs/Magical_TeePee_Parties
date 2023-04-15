from django.contrib import admin
from .models import Post, Comment, PostGallery, Image, PostProducts, BookAParty
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Create an admin panel to write a post using summer notes
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Create an admin panel to administer comments in posts
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    # Allows to approve comments
    def approve_comments(self, request, queryset): 
        queryset.update(approved=True)


class GalleryImageInline(admin.TabularInline):
    """
    Allows to add more than one image in a gallery
    """
    model = PostGallery.images.through


class ProductImageInline(admin.TabularInline):
    """
    Allows to add more than one image in product description section
    """
    model = PostProducts.images.through


@admin.register(PostGallery)
class GalleryImageAdmin(SummernoteModelAdmin):
    """
    Create an admin panel to make galleries
    """
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
    """
    Create an admin panel to add images, then these images can be used in 
    galleries or Product descriptions
    """
    list_display = ('id', 'image')


@admin.register(PostProducts)
class ProductsImageAdmin(SummernoteModelAdmin):
    """
    Create an admin panel to make content for the products section
    """
    list_display = ('title', 'slug', 'title_image')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]
    summernote_fields = ('description', 'excerpt')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'title_image', 'description',
                       'excerpt')
        }),
    )


@admin.register(BookAParty)
class BookAPartyAdmin(admin.ModelAdmin):
    """
    Create an admin panel to administer the 'Book a party' section
    """
    list_display = ('party_theme', 'number_of_teepees', 'city', 'date',
                    'approved', 'host', 'price')
    list_filter = ('approved', 'party_theme', 'date')
    search_fields = ('city', 'date', 'email', 'phone_number')
    actions = ['approve_party']

    # Allows to approve parties
    def approve_party(self, request, queryset):
        queryset.update(approved=True)
