from django.contrib import admin
from django.urls import path, include

from book import urls as book_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/books/", include(book_urls))
]
