from django.shortcuts import render
from rest_framework import viewsets

from .models import Book, Subject
from .serializers import BookSerializer, SubjectSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
