from django.urls import path
from . import views

app_name = "bookstore"

urlpatterns = [
    path("", views.book_list, name="book-list"),
    path("book_list/", views.book_list, name="book-list"),
    path("book_details/<int:book_id>/", views.book_details, name="book-details"),
    path("book_delete/<int:book_id>/delete/", views.book_delete, name="book-delete"),
    path("book_update/<int:book_id>/update/", views.book_update, name="book-update"),
    path("create/", views.book_create, name="book-create"),
]
