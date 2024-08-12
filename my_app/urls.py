from django.urls import path
from .views import IndexView, PostDetailView, TaggedPostListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('tags/<slug:slug>/', TaggedPostListView.as_view(), name='tagged_posts'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)