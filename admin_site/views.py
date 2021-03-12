from django.shortcuts import render, redirect
from admin_site.forms import BlogPostForm
from .models import BlogPost
from django.http import JsonResponse


# Create your views here.

def Dashboard(request):
    return render(request, 'admin/contents/dashboard.html')


def WritePost(request):
    if request.method == 'POST':
        post_form = BlogPostForm(request.POST, request.FILES)

        if post_form.is_valid():
            blog = BlogPost()
            blog.title = post_form.cleaned_data['title']
            blog.images = post_form.cleaned_data['image']
            blog.details = post_form.cleaned_data['details']

            blog.save()
            return redirect('write-post')
    else:
        post_form = BlogPostForm()
    # return JsonResponse(context, safe=False)
    return render(request, 'admin/contents/write_blog.html')


def ManagePost(request):
    posts = BlogPost.objects.all().order_by('-id')

    count = 1
    count += 1
    context = {
        'posts': posts,
        'count': count
    }
    return render(request, 'admin/contents/manage_post.html', context)


def EditPost(request, pk):
    post = BlogPost.objects.get(id=pk)
    context = {
        'post': post
    }
    # return JsonResponse(context, safe=False)
    return render(request, 'admin/contents/edit_post.html', context)
