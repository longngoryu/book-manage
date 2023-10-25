from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from book import urls as book_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/books/", include(book_urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
