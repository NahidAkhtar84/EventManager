from django.shortcuts import render
from django.views import View
from .models import about_us
# Create your views here.

class AboutUs(View):
    def get(self, request):
        aboutus = about_us.objects.first()
        context = {
            'aboutus': aboutus,
        }
        return render(request, 'index/aboutus.html', context)
