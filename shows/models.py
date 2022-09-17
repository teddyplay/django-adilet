from django.db import models


class Book_detail(models.Model):
    GENRE_CHOICES = (
        ("Comedy", "COMEDY"),
        ("Horror", "HORROR"),
        ("Fantasy", "FANTASY"),
        ("Romans", "ROMANS"),
    )
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    quantity = models.PositiveIntegerField()
    create_date = models.TimeField(auto_now_add=True)
    update_date = models.TimeField(auto_now=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    duration = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title
class BookComment(models.Model):
    text = models.TextField(max_length=1000)
    create_date = models.TimeField(auto_now_add=True)
    update_date = models.TimeField(auto_now=True)
    books = models.ForeignKey(Book_detail,
                              on_delete=models.CASCADE,related_name="book_comment")


    def __str__(self):
        return self.books.title

