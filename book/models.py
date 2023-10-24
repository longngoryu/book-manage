from django.db import models
import uuid


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=50
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity_in_stock = models.IntegerField()
    publication_date = models.DateField()
    image_url = models.ImageField(upload_to="images/books/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.title


class BookReview(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=50
    )
    related_book = models.CharField(max_length=255)
    related_user = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.CharField(max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)

    def __str__(self):
        return self.related_book


class BookHistory(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=50
    )
    related_book = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    edit_info = models.CharField(max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)

    def __str__(self):
        return self.related_book