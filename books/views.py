from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, BookUpdateSerializer
from .models import Book


class BookView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdate(generics.UpdateAPIView):
    serializer_class = BookUpdateSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'

