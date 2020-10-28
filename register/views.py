from django.shortcuts import render, redirect
from .forms import RegisterForm, EditForm
from django.views import View
from django.http import HttpResponseRedirect


class RegisterView(View):
    form = RegisterForm
    template_name = 'register/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
        
        return render(request, self.template_name, {'form': form})


class EditUserView(View):
    form = EditForm
    template_name = 'edit/edit_user.html'

    def get(self, request, *args, **kwargs):
        form = self.form
        return render(request, self.template_name, {'form': form})