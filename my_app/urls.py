from django.urls import path
from .views import PostListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)