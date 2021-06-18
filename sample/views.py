from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Book, Author

# Create your views here.


class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view()

# CRUD
"""
Create: データを作成する（CreateView）
Read: データを読み取る: ListView（複数のデータ）, DetailView（一つのデータを読み取る）
Update: データを更新する（UpdateView）
Delete: データを削除する（DeleteView）
"""


class BookListView(ListView):

    template_name = 'book/list.html'
    # model = Book
    queryset = None
    context_object_name = 'books'
    paginate_by = 15

    def get_queryset(self):
        date = self.request.GET.get('date')
        books = Book.objects.filter(create__gte=date)
        return books

book_list = BookListView.as_view()


class BookDetailView(DetailView):

    template_name = 'book/detail.html'
    model = Book
    context_object_name = 'book'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_uuid = self.kwargs['uuid']
        authors = Author.objects.filter(book__uuid=book_uuid)
        context['authors'] = authors
        return context

    def post(self, request, *args, **kwargs):
        post = request.POST
        book_title = post.get('title')
        book_description = post.get('descriotion')
        book_uuid = self.kwargs['uuid']
        Book.objects.filter(uuid=book_uuid).update(title=book_title, description=book_description)
        success_url = request.META['HTTP_REFERER']
        return HttpResponseRedirect(success_url)

book_detail = BookDetailView.as_view()


class BookFormViewBase:

    template_name = 'book/form.html'
    model = Book
    fields = ('title', 'description')
    success_url = reverse_lazy('sample:book_list') # /books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = self.text
        return context


class BookCreateView(BookFormViewBase, CreateView):

    text = '作成'

book_create = BookCreateView.as_view()


class BookUpdateView(BookFormViewBase, UpdateView):

    text = '更新'

book_update = BookUpdateView.as_view()


class AuthorAddView(CreateView):

    template_name = 'book/author/create.html'
    model = Author
    fields = ('name',)
    success_url = reverse_lazy('sample:book_list')

    def form_valid(self, form):
        author = form.save(commit=False)
        book_id = self.kwargs['pk']
        author.book_id = book_id
        author.save()
        book_uuid = Book.objects.values_list('uuid', flat=True).get(id=book_id)
        self.success_url = reverse_lazy('sample:book_detail', kwargs={'uuid': book_uuid})
        return super().form_valid(form)

author_add = AuthorAddView.as_view()