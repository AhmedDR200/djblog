from django.shortcuts import render
from .models import Post
from .forms import Postform
from django.views.generic import ListView , DetailView
from django.views.generic import CreateView , DeleteView , UpdateView

# Create your views here.






def post_list(request):
    all_posts =Post.objects.all() 
    return render(request, 'post/post_list.html', {'all_posts': all_posts})


def post_datail(request  ,id):
    post = Post.objects.get(id=id)
    return render(request, 'post/post_detail.html', {'post': post})



def post_create(request):
    if request.method =="POST":
     form = Postform(request.POST)
     if form.is_valid():
         form.save()

    else:
         form = Postform()
    return render(request ,'post/post_create.html' , {'form':form} )


def post_edit(request , id):
    post = Post.objects.get(id=id)
    if request.method =="POST":
     form = Postform( request.POST , instance=post)
     if form.is_valid():
         form.save()

    else:
         form = Postform(instance=post)
    return render(request ,'post/post_edit.html' , {'form':form} )



class PostList(ListView):
    model = Post


class PostDetail(DetailView):
   model = Post


class PostUpdate(UpdateView):
    model = Post
    fields = ['title','contant','created_at']
    template_name ='post/post_edit.html'
    success_url='/blog/cbv'



class PostCreate(CreateView):
    model = Post
    fields = ['title','contant','created_at','email','views_count']
    template_name ='post/post_create.html'
    success_url='/blog/cbv'
