from django.shortcuts import render
from event_booking.models import Events
import datetime
from django.core.paginator import Paginator, EmptyPage
from admin_site.models import BlogPost
from django.http import JsonResponse


# Create your views here.

def Index(request):
    all_events = Events.objects.filter(status='accepted')
    recent_events = Events.objects.filter(status='accepted').filter(start__gte=datetime.datetime.now()).order_by(
        '-start')
    firstblog = BlogPost.objects.all().order_by('date')[0]
    blogs = BlogPost.objects.all().order_by('date')[1:3]

    page = request.GET.get('page', 1)
    paginator = Paginator(recent_events, 3)

    try:
        recent_events = paginator.page(page)
    except EmptyPage:
        recent_events = paginator.page(paginator.num_pages)

    context = {
        "events": all_events,
        "recent_events": recent_events,
        "blogs": blogs,
        "firstblog": firstblog,
    }
    # return JsonResponse(context, safe=False)
    return render(request, 'index/index.html', context)


def BlogDetails(request, slug):
    details_post = BlogPost.objects.get(slug=slug)
    related = BlogPost.objects.filter(category=str(details_post.category)).exclude(title=str(details_post.title)).all() \
                  .order_by('date')[0:3]

    context = {
        'details': details_post,

        'related': related,
    }
    # return JsonResponse(context, safe=False)
    return render(request, 'index/blog_details.html', context)
