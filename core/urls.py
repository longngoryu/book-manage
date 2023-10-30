from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from book import urls as book_urls
from user import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/books/", include(book_urls)),
    path("api/users/", include(user_urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
