from django.contrib import admin
from . import models


admin.site.register(models.Book_detail)
admin.site.register(models.BookComment)
