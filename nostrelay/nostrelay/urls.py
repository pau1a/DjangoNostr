from django.contrib import admin
from django.urls import path
from django.conf import settings
from therelay.views import list_open_websockets
from django.conf.urls.static import static

urlpatterns = [
    path('list-open-websockets/', list_open_websockets, name='list_open_websockets'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
