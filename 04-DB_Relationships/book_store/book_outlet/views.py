from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('title')
    tot_num_of_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'tot_num_of_books': tot_num_of_books,
        'avg_rating': avg_rating,
    })

def book_detail(request, id):

    # If id does not exist, exception will raised and catch and 404 will be rendered

    # Method 1
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    #Method 2
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book_outlet/book_details.html', {
        'title': book.title,
        'rating': book.rating,
        'author': book.author,
        'is_bestseller': book.is_bestselling,
    })

def book_detail_slug(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_details.html', {
        'title': book.title,
        'rating': book.rating,
        'author': book.author,
        'is_bestseller': book.is_bestselling,
    })