from django.shortcuts import render,redirect
from .models import Post


# Create your views here.

def index(request):
    if(request.method=='POST'):
        title=request.POST["title"]
        details=request.POST["details"]
        post=Post.objects.create(title=title,details=details)
        post.save();
        return redirect('/')
    else:
        posts = Post.objects.all()
        return render(request, 'index.html', {'posts': posts})


def post(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': posts})

