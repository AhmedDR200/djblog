from django.shortcuts import render
from .models import Post
# Create your views here.






def post_list(request):
    all_posts =Post.objects.all() 
    return render(request, 'post/post_list.html', {'all_posts': all_posts})


def post_datail(request  ,id):
    post = Post.objects.get(id=id)
    return render(request, 'post/post_detail.html', {'post': post})