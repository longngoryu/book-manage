from django.urls import path
from .views import BookApiView, BookDetailApiView

urlpatterns = [
  path("", BookApiView.as_view()),
  path("<str:book_id>/", BookDetailApiView.as_view()),
]