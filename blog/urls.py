from . import views
from django.urls import path
from .views import GalleryListView, SeeGalleryView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('gallery/<slug:slug>/', SeeGalleryView.as_view(), name='see_gallery'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]