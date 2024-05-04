
from django.shortcuts import render, redirect
from .models import Book
from .crud_operations import create_book, get_all_books, get_book_by_id, update_book, delete_book

def book_list(request):
    books = get_all_books()
    return render(request, "bookstore/book_list.html", {"books": books})

def book_details(request, book_id):
    book = get_book_by_id(book_id)
    return render(request, "bookstore/book_details.html", {"book": book})

def book_delete(request, book_id):
    if request.method == "POST":
        delete_book(book_id)
        return redirect("bookstore:book-list")
    else:
        return redirect("bookstore:book-list")


def book_update(request, book_id):
    book = get_book_by_id(book_id)
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        rate = request.POST.get("rate")
        views = request.POST.get("views")
        update_book(book_id, title=title, desc=desc, rate=rate, views=views)
        return redirect("bookstore:book-list")
    return render(request, "bookstore/book_update.html", {"book": book})

def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        rate = request.POST.get("rate")
        views = request.POST.get("views")
        create_book(title=title, desc=desc, rate=rate, views=views)
        return redirect("bookstore:book-list")
    return render(request, "bookstore/book_create.html")
