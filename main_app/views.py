from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from .models import Widget


# Create your views here.
def home(request): 
  return HttpResponse('<h1>Wacky Widgets</h1>')

def about(request):
  return render(request, 'about.html')


class WidgetCreate(CreateView):
  model = Widget
  fields = ['Description', 'Quantity']

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/about/'