from django.shortcuts import render

# Create your views here.

def post_list(reqeust):
    return render(reqeust, 'blog/post_list.html', {})
