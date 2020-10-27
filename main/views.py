from django.shortcuts import render

# Create your views here.

def main(response):
    return render(response, 'main/main.html')