from django.shortcuts import render, get_object_or_404
from . import models



def book_show(request):
    books = models.Book_detail.objects.all()
    return render(request, "all_books.html", {"books": books})



def book_detail(request, id):
    show = get_object_or_404(models.Book_detail, id=id)
    return render(request, "shows_detail.html", {"book": show})

def dilhan_loh(request):
    return render(request, 'dilhan_pidoras.html')