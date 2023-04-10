from . import views
from django.urls import path
from .views import GalleryListView, SeeGalleryView, ProductsListView, ProductView, ContactUsView, AboutUsView, BookAPartyView, submitted_parties, EditPartyView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contactus/', ContactUsView.as_view(), name='contactus'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('gallery/<slug:slug>/', SeeGalleryView.as_view(), name='see_gallery'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/<slug:slug>/', ProductView.as_view(), name='products_detail'),
    path('bookapaty/', BookAPartyView.as_view(), name='book_a_paty'),
    path('submitted-parties/', submitted_parties, name='submitted_parties'),
    path('submitted-parties/<slug:order_nr>/edit/', EditPartyView.as_view(), name='edit_party'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]