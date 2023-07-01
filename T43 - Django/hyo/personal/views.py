from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def online_shop(request):
    return render(request, 'online_shopping.html')

def index(request):
    return render(request, 'index.html')

def about_me(request):
    return render(request, 'about me.html')