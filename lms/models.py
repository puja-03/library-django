from django.db import models

# Create your models here.
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    phoneno = models.IntegerField(default=0)
    course = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    bookid = models.CharField(max_length=100)
    image = models.ImageField(upload_to="book/")
    booktitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.BooleanField(default=True)
    publication = models.CharField(max_length=100)
    def __str__(self):
        return self.bookid