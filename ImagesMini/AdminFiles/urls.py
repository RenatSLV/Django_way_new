from django.contrib import admin
from django.urls import path
from App1.views import upload_image, show_images
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_image, name='upload_image'),
    path('gallery/', show_images, name='show_images'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
