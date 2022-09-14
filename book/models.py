from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    img = models.ImageField(upload_to="", null=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    author = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.title


