from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        serializer = BookSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "title": request.data.get("title"),
            "author": request.data.get("author"),
            "description": request.data.get("description"),
            "price": request.data.get("price"),
            "quantity_in_stock": request.data.get("quantity_in_stock"),
            "publication_date": request.data.get("publication_date"),
            "image_url": request.data.get("image_url"),
        }
        
        serializer = BookSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       