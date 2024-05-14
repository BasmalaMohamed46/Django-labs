from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Book, Category
from .crud_operations import create_book, get_all_books, get_book_by_id, update_book, delete_book
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "categories"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 10 or len(title) > 50:
            raise ValidationError("Title must be between 10 and 50 characters.")
        return title

    def clean_categories(self):
        categories = self.cleaned_data.get("categories")
        if len(categories) < 1:
            raise ValidationError("Please select at least one categories.")
        return categories
    
@login_required
def book_list(request):
    books = Book.objects.all()
    user = request.user  
    return render(request, "bookstore/book_list.html", {"books": books, "user": user})

def book_details(request, book_id):
    book = get_book_by_id(book_id)
    return render(request, "bookstore/book_details.html", {"book": book})

@permission_required('Bookstore.delete_book', raise_exception=True)
@login_required
def book_delete(request, book_id):
    if request.method == "POST":
        book = get_book_by_id(book_id)
        book.delete()
        return redirect("bookstore:book-list")
    else:
        return redirect("bookstore:book-list")
    
   
@login_required
def book_update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    categories = Category.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookstore:book-list")
    else:
        form = BookForm(instance=book)
        selected_category_ids = book.categories.values_list('id', flat=True)
        form.fields['categories'].initial = selected_category_ids
    return render(request, "bookstore/book_update.html", {"form": form, "categories": categories})


@login_required
def book_create(request):
    categories = Category.objects.all()
    categories_ids = request.POST.getlist("categories")
    categories = Category.objects.filter(pk__in=categories_ids)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("bookstore:book-list")
    else:
        form = BookForm()
    return render(request, "bookstore/book_create.html", {"form": form, "categories": categories})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("bookstore:book-list")
    else:
        form = AuthenticationForm()
    return render(request, 'bookstore/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('bookstore:book-list')
    else:
        form = UserCreationForm()
    return render(request, 'bookstore/signup.html', {'form': form})

