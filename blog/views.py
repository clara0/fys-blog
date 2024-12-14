from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

# Create your views here.
def blog_home(request):
    # - means largest date is displayed first
    posts = Post.objects.all().order_by("-created")
    context = {
        "posts" : posts,
    }
    return render(request, "blog/home.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                text = form.cleaned_data["body"],
                post = post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post = post)
    context = {
        "post" : post,
        "comments" : comments,
        "form" : CommentForm(),
    }

    return render(request, "blog/detail.html", context)
