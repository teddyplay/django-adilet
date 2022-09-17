from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from . import models,forms



def book_show(request):
    books = models.Book_detail.objects.all()
    return render(request, "all_books.html", {"books": books})



def book_detail(request, id):
    show = get_object_or_404(models.Book_detail, id=id)
    return render(request, "shows_detail.html", {"book": show})



def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Форма успешна создана!")
    else:
        form = forms.BookForm()

    return render(request,"add_book.html", {"form":form})




