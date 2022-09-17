from django.urls import path, include
from . import views


urlpatterns = [
    path('shows/', views.book_show),
    path('shows/<int:id>/', views.book_detail),
    path('add-book/', views.add_book, ),

]
