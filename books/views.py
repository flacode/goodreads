from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .serializers import BookSerializer, BookUpdateSerializer, UserSerializer
from .models import Book
from .permissions import IsOwner


class BookView(generics.ListCreateAPIView):
    """
    post: Add a new book to the collection of books.
    get: Return a list of books belonging to the current user
    """
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

class BookUpdate(generics.UpdateAPIView):
    """
    put: Update the current page for a book they own.
    """
    serializer_class = BookUpdateSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'
    permission_classes = (IsOwner, )


class UserSignUp(generics.CreateAPIView):
    """
    post: Create a new user account.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
