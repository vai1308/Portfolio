from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    current_time = datetime.now()
    return render(request, 'data/index.html', {'current_time': current_time})
def contact(request):
    return render(request, 'data/contact.html')
def projects(request):
    return render(request, 'data/projects.html')
def about(request):
    return render(request, 'data/about.html')
def thankyou(request):
    return render(request, 'data/thankyou.html')