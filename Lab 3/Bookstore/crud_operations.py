from .models import Book, Category

def create_book(title, author, user, categories=None):
    book = Book.objects.create(title=title, author=author, user=user)
    if categories:
        book.categories.set(categories)
    return book

def get_all_books():
    return Book.objects.all()

def get_book_by_id(book_id):
    try:
        return Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return None

def update_book(book_id, title=None, author=None, user=None, categories=None):
    book = get_book_by_id(book_id)
    if book:
        if title is not None:
            book.title = title
        if author is not None:
            book.author = author
        if user is not None:
            book.user = user
        if categories is not None:
            book.categories.set(categories)
        book.save()
        return book
    return None

def delete_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        book.delete()
        return True
    return False
