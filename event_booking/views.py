from django.shortcuts import render


# Create your views here.
from django.http import JsonResponse
from event_booking.models import Events
from django.views import View
from django.shortcuts import render, redirect
# Create your views here.




def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


class EventBook(View):
    def get(self, request):
        return render(request, 'index/event_booking.html')

    def post(self, request):
        if request.method == 'POST':
            pst = request.POST
            name = pst.get('eventname')
            username = pst.get('username')
            phone = pst.get('mobilenumber')
            email = pst.get('email')
            start_date = pst.get('startdate')
            end_date = pst.get('enddate')
            print("This is: ", start_date)
            event = Events(
                name=name,
                username=username,
                phone=phone,
                email=email,
                start=start_date,
                end=end_date
            )

            event.save()
            return redirect('index')