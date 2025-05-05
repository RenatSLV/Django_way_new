from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App1.views import upload_document, document_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_document, name='upload_document'),
    path('', document_list, name='document_list'),
]

# Только для разработки!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
