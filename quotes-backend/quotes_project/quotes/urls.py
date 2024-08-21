# quotes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('quotes/', views.QuoteList.as_view(), name='quote-list'),
    path('quotes/<int:pk>/', views.QuoteDetail.as_view(), name='quote-detail'),
]
