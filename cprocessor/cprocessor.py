from general.models import sociallinks, copyright
from django.http import JsonResponse

def context_processor(request):
    social = sociallinks.objects.all()
    cpyright = copyright.objects.first()
    contextview = {
        'social': social,
        'cpyright': cpyright,
    }

    return contextview