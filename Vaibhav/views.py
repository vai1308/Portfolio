from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'data/main.html')
def contact(request):
    return render(request, 'data/contact.html')
def projects(request):
    return render(request, 'data/projects.html')
def about(request):
    return render(request, 'data/about.html')
def thankyou(request):
    return render(request, 'data/thankyou.html')
def submit_form(request):
    if request.method == 'POST':
        return redirect('thankyou')