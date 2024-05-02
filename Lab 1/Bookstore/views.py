from django.shortcuts import render, redirect


def index(request):
    return render(request, "main/base_layout.html")

books = [

]


def _get_book(book_id):
    for book in books:
        if "id" in book and book["id"] == book_id:
            return book
    return None


def book_list(request):
    my_context = {"books": books}
    return render(request, "bookstore/book_list.html", context=my_context)


def book_details(request, **kwargs):
    book_id = kwargs.get("book_id")
    book = _get_book(book_id)
    if book:
        my_context = {"book": book}
        return render(request, "bookstore/book_details.html", context=my_context)
    else:
        return render(
            request, "bookstore/error.html", {"error_message": "Book not found"}
        )


def book_delete(request, **kwargs):
    book_id = kwargs.get("book_id")
    book = _get_book(book_id)
    if book:
        books.remove(book)
        my_context = {"books": books}
        return render(request, "bookstore/book_list.html", context=my_context)
    else:
        return render(
            request, "bookstore/error.html", {"error_message": "Book not found"}
        )


def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        genre = request.POST.get("genre")
        publication_year = request.POST.get("publication_year")
        if title and author and genre and publication_year:
            new_book = {
                "id": len(books) + 1,
                "title": title,
                "author": author,
                "genre": genre,
                "publication_year": int(publication_year),
            }
            books.append(new_book)
            my_context = {"books": books}
            return render(request, "bookstore/book_list.html", context=my_context)
        else:
            return render(
                request, "bookstore/error.html", {"error_message": "Invalid form data"}
            )
    else:
        return render(request, "bookstore/book_create.html")
def book_update(request, **kwargs):
    book_id = kwargs.get("book_id")
    book = _get_book(book_id)
    if request.method == "POST":
        if book:
            title = request.POST.get("title")
            author = request.POST.get("author")
            genre = request.POST.get("genre")
            publication_year = request.POST.get("publication_year")
            if title and author and genre and publication_year:
                book["title"] = title
                book["author"] = author
                book["genre"] = genre
                book["publication_year"] = int(publication_year)
                my_context = {"books": books}
                return render(request, "bookstore/book_list.html", context=my_context)
            else:
                return render(
                    request, "bookstore/error.html", {"error_message": "Invalid form data"}
                )
        else:
            return render(
                request, "bookstore/error.html", {"error_message": "Book not found"}
            )
    else:
        if book:
            my_context = {"book": book}
            return render(request, "bookstore/book_update.html", context=my_context)
        else:
            return render(
                request, "bookstore/error.html", {"error_message": "Book not found"}
            )
