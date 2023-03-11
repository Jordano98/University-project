from django.urls import path
from .views import UniListView,UniDetailView
urlpatterns = [
    path('',UniListView.as_view(),name = 'uni-list'),
    path('university/<int:pk>/',UniDetailView.as_view(),name = 'uni-detail'),
]