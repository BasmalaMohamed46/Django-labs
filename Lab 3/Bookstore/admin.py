from django.contrib import admin
from .models import Book, Category
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "isbn_number", "user")
    list_filter = ("user", "categories")
    search_fields = ("title", "author")
    formfield_overrides = {
        models.CharField: {'validators': [MinLengthValidator(10), MaxLengthValidator(50)]},
    }

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    formfield_overrides = {
        models.CharField: {'validators': [MinLengthValidator(2)]},
    }

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
