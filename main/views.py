from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

class Main(generic.CreateView):
    template_name = 'main/main.html'
    success_url = reverse_lazy('main.html')