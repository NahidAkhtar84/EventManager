from django.shortcuts import render


# Create your views here.

def calendar(request):
    template = 'calendar.html'
    context = {}
    return render(request, template, context)
