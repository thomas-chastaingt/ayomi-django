from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

#similar elements
class Main(View):
    template_name = 'main/main.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Main_home(View):
    template_name = 'home/home.html'
    
    def get(self, request, *arfs, **kwargs):
        return render(request, self.template_name)