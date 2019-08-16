from django.urls import path
from .views import EventListView,EventDetailView,EventCreateView,EventUpdateView,EventDeleteView

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('new/', EventCreateView, name='event-create'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]