from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemViewSet (viewsets.ViewSet):
