from django.shortcuts import render
from events.models import Event
from causes.models import Cause
def index(request):
    events = Event.objects.all()
    causes = Cause.objects.all()
    context = {
        'events': events[:4],
        'causes': causes[:3]
    }
    return render(request, 'index.html',context)


def blog(request):
    return render(request, 'blog.html',{})


def aboutUs(request):
    return render(request, 'about-us.html',{})


def causes(request):
    return render(request, 'causes.html',{})


def contact(request):
    return render(request, 'contact.html',{})


def elements(request):
    return render(request, 'elements.html',{})


def eventDetails(request):
    return render(request, 'event-details.html',{})


def events(request):
    return render(request, 'events.html',{})


def singleBlog(request):
    return render(request, 'single-blog.html',{})
