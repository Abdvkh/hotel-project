from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('djeym/', include('djeym.urls', namespace='djeym')),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
