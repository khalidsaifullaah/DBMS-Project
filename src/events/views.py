from django.shortcuts import render,redirect
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Event
from .forms import EventCreateForm

# Create your views here.

class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events.html'
    ordering = ['-date_posted']


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'


@login_required
def EventCreateView(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST,request.FILES)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventCreateForm()
    context ={
        'form': form
    }
    return render(request, 'event_create.html',context)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    template_name = 'event_create.html'
    fields = ['title', 'about', 'area', 'eventTime', 'thumbnail']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Cause = self.get_object()
        if self.request.user == Cause.author:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = '/events'
    def test_func(self):
        Cause = self.get_object()
        if self.request.user == Cause.author:
            return True
        return False