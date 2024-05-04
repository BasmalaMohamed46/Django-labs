from .models import Book


def create_book(title, desc, rate, views=0):
    book = Book.objects.create(title=title, desc=desc, rate=rate, views=views)
    return book


def get_all_books():
    return Book.objects.all()

def get_book_by_id(book_id):
    try:
        return Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return None


def update_book(book_id, title=None, desc=None, rate=None, views=None):
    book = get_book_by_id(book_id)
    if book:
        if title is not None:
            book.title = title
        if desc is not None:
            book.desc = desc
        if rate is not None:
            book.rate = rate
        if views is not None:
            book.views = views
        book.save()
        return book
    return None


def delete_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        book.delete()
        return True
    return False
