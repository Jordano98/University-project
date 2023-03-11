from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import University
# Create your views here.

class UniListView(ListView):
    paginate_by = 2
    model = University
    queryset = University.objects.all()
    
    context_object_name = 'unis'

class UniDetailView(DetailView):
    
    model = University

