from django.contrib import admin
from .models import Book, BookReview, BookHistory

admin.site.register([Book, BookReview, BookHistory])