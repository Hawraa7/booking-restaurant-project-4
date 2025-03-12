from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menu_view(request):
    # menu_items = MenuItem.objects.all()
    return HttpResponse('Here is the menu')