from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'data/index.html')
def contact(request):
    return render(request, 'data/contact.html')
def projects(request):
    return render(request, 'data/projects.html')
def about(request):
    return render(request, 'data/about.html')
def thankyou(request):
    return render(request, 'data/thankyou.html')