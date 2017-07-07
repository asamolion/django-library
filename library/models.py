from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=250)
    call_no = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    pub_date = models.DateField()
    edition = models.IntegerField()
    borrower = models.ForeignKey(User, blank=True, null=True)


class Subject(models.Model):
    title = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='subjects')
