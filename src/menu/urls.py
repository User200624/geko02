from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('menu/<int:pk>/', MenuDetialView.as_view(), name='menu_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]