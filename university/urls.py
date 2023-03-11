from django.urls import path
from .views import UniListView,UniDetailView,uni_search

app_name= 'university'

urlpatterns = [
    path('',UniListView.as_view(),name = 'uni-list'),
    path('university/<int:pk>/',UniDetailView.as_view(),name = 'uni-detail'),
    path('search/',uni_search,name="search"),
]