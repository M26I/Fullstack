from django.shortcuts import render
from .models import Menu
from .models import Booking
from .serializers import MenuItemSerializer
from .serializers import BookingSerializer
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer