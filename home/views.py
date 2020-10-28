from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy

# Create your views here.

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'home/home.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user