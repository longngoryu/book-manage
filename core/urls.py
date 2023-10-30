from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

from book import urls as book_urls
from user import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/books/", include(book_urls)),
    path("api/users/", include(user_urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
