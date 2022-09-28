from django.shortcuts import render
from django.views import generic
from post.forms import CreatePostForm
from post.models import Post
from django.urls import reverse
from django.db.models import Q
# Create your views here.


def index_page(request):
    title = request.GET.get('title')
    posts = Post.objects.all()
    if title:
        posts = Post.objects.filter(Q(name__icontains=title) |
                                    Q(description__icontains=title)
                                    )
    return render(request, "index.html", locals())

class CreatePostView(generic.CreateView):
    template_name = 'create_post.html'
    model = Post
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

class DetailPostView(generic.DetailView):
    template_name = 'detail_post.html'
    model = Post
    context_object_name = "post"

    def get_success_url(self):
        return reverse('')

    # post: Post.objects.get(id=1)


