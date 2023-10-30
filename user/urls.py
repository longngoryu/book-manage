from django.urls import path
from .views import UserApiView, RegisterApiView, LoginApiView

urlpatterns = [
  path("", UserApiView.as_view()),
  path("register/", RegisterApiView.as_view()),
  path("login/", LoginApiView.as_view()),
]