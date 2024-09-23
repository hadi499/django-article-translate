from django.shortcuts import render
from .models import Page, Book

def books_view(request):
  return render(request, 'books.html')


def ss7_view(request):
  words = Page.objects.all()
  return render(request, 'pages/ss7.html', {'words': words})

from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    # Mengambil semua Book dari database
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    # Mengambil instance Book tertentu berdasarkan ID
    book = get_object_or_404(Book, id=book_id)
    
    # Mengambil semua Page yang terkait dengan Book ini
    pages = book.page_set.all()  # atau bisa juga book.pages.all() jika Anda menambahkan related_name
    
    return render(request, 'book_detail.html', {'book': book, 'pages': pages})