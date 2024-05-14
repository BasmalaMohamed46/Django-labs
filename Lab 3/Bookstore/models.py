from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
import uuid
from django.contrib.auth.models import Permission



class Category(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100, validators=[MinLengthValidator(10), MaxLengthValidator(50)])
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name="books")

    def __str__(self):
        return self.title

delete_book_permission = Permission.objects.get(codename='delete_book')
