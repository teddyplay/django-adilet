from django.shortcuts import render
from django.http import HttpResponse
from . import models


def hello_world(request):
    return HttpResponse('<h2>Привет Мир!)</h2>')

def post_all(request, id):
    post = models.Post.objects, id=id
    return render(request, 'post_list.html', {"post": post})