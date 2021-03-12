from django.shortcuts import render, redirect
from admin_site.forms import BlogPostForm
from .models import BlogPost
import os
from datetime import date
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

        return redirect('manage-post')
    else:
        post_form = BlogPostForm()
    # return JsonResponse(context, safe=False)
    return render(request, 'admin/contents/write_blog.html')


def ManagePost(request):
    posts = BlogPost.objects.all().order_by('-id')

    context = {
        'posts': posts,
    }
    return render(request, 'admin/contents/manage_post.html', context)


def EditPost(request, pk):
    post = BlogPost.objects.get(id=pk)

    form = BlogPostForm(request.POST, request.FILES)

    img = request.FILES.get('image')
    if img:
        if form.is_valid():
            blog = BlogPost(id=pk)
            blog.title = form.cleaned_data['title']
            blog.images = form.cleaned_data['image']
            blog.details = form.cleaned_data['details']
            blog.date = date.today()

            # deleting old uploaded image.
            image_path = post.images.path
            if os.path.exists(image_path):
                os.remove(image_path)

            blog.save()
            return redirect("manage-post")
    else:
        if request.method == 'POST':
            title = request.POST.get('title')
            c_image = request.POST.get('current_image')
            details = request.POST.get('details')

            BlogPost.objects.filter(id=pk).update(title=title, images=c_image, details=details, date=date.today())
            return redirect("manage-post")

    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     image = request.FILES.get('image')
    #     c_image = request.POST.get('current_image')
    #     details = request.POST.get('details')
    #
    #     print(image)
    #
    #     context = {
    #         't': title,
    #         'img': str(image),
    #         'c_img': c_image,
    #         'd': details
    #     }
    #     return JsonResponse(context, safe=False)

    context = {
        'post': post
    }
    # return JsonResponse(context, safe=False)
    return render(request, 'admin/contents/edit_post.html', context)


def DeletePost(request, pk):
    BlogPost.objects.get(id=pk).delete()
    return redirect('manage-post')
