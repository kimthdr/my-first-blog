from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(reqeust):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(reqeust, 'blog/post_list.html', {'posts':posts})

def post_detail(reqeust, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(reqeust, 'blog/post_detail.html', {'post':post})
