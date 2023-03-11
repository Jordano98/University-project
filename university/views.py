from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
import django_filters
from .models import University
# Create your views here.

class UniFilter(django_filters.FilterSet):
    class Meta:
        model = University
        fields = ["city"]


class UniListView(ListView):
    paginate_by = 2
    model = University
    context_object_name = 'unis'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = UniFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = UniFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context
    

class UniDetailView(DetailView):
    
    model = University

    context_object_name = 'uni'


def uni_search(request):
    unis=University.objects.all()
    if request.method == 'GET':
        if x := request.GET.get('s') :
            name = unis.filter(name__contains=x)
            city = unis.filter(city__name__contains=x)
            country = unis.filter(city__country__name__contains=x)
            if name: 
                unis=name
            elif city:
                unis = city
            elif country:
                unis =country
            
    context={'unis':unis }
    return render(request,'university/university_list.html',context)