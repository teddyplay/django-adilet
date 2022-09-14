from django.urls import path, include
from . import views


urlpatterns = [
    path('hello/', views.hello_world),
    path('post_all/', views.post_all),


]
