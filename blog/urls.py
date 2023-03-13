from . import views
from django.urls import path
from .views import GalleryListView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]