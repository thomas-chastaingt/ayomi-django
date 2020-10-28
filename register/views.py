from django.shortcuts import render, redirect
from .forms import RegisterForm, EditForm
from django.views import View
from django.http import HttpResponseRedirect

# class to show register template and to submit a new user
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

#class to edit your own informations
class EditUserView(View):
    form = EditForm
    template_name = 'edit/edit_user.html'

    def get(self, request, *args, **kwargs):
        form = self.form
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form})
        
        return render(request, self.template_name, {'form': form})