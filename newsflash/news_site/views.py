import random
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Post, Tag, Author
from django.shortcuts import get_object_or_404
from django.db.models import Q


# Create your views here.
class IndexpageView(ListView):
    template_name = "news_site/index.html"
    model = Post
    context_object_name = 'cheese'
    paginate_by = 5
    ordering = ['-date']

class AllpagesView(ListView):
    template_name = "news_site/allpages.html"
    model = Post
    context_object_name = 'post'

class PostDetailView(DetailView):
    model = Post
    template_name = 'news_site/news_post.html'
    context_object_name = 'post'

def cheese_page(request):
    return render(request, 'news_site/cheese.html')

def cheese_manifesto(request):
    return render(request, 'news_site/cheese_manifesto.html') 

def search_view(request):
    search_query = request.GET.get('s')
    if search_query:
        results = Post.objects.filter(
    Q(post_field__icontains=search_query) | Q(title__icontains=search_query)
)
    
    return render(request, 'news_site/search_results.html', {'results': results, 'search_query': search_query})


def author_posts(request, author_slug):
    author = get_object_or_404(Author, slug=author_slug)
    posts = Post.objects.filter(author=author)
    context = {
        'author': author,
        'posts': posts,
    }
    return render(request, 'news_site/author_list.html', context)

def tag_post_list(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.post_set.all()
    context = {
        'tag': tag,
        'posts': posts,
    }
    
    return render(request, 'news_site/tag_posts_list.html', context)

def random_page(request):
    slugs = Post.objects.values_list('slug', flat=True)
    random_slug = random.choice(slugs)
    return redirect("post-detail-page", slug = random_slug)


