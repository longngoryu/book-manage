from rest_framework import serializers
from .models import Book, BookReview, BookHistory

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "description",
            "price",
            "quantity_in_stock",
            "publication_date",
            "image_url",
            "created_at",
        )


class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = (
            "id",
            "related_book",
            "related_user",
            "rating",
            "comment",
            "created_at",
        )


class BookHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookHistory
        fields = (
            "id",
            "related_book",
            "user",
            "edit_info",
            "created_at",
        )