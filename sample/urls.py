from django.urls import path
from . import views

app_name= 'sample'
urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.book_list, name='book_list'),
    path('books/<uuid:uuid>', views.book_detail, name='book_detail'),
    path('books/create', views.book_create, name='book_create'),
    path('books/update/<int:pk>', views.book_update, name='book_update'),
    path('books/<int:pk>/author/add', views.author_add, name='author_add'),
]