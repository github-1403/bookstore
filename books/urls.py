from django.urls import path
from . import views

urlpatterns = [
    path('books_list/', views.BookListView.as_view(), name='books_list')
]
