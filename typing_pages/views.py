from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'typing_pages/index.html')

def about(request):
    return render(request, 'typing_pages/about.html')

def contact(request):
    return render(request, 'typing_pages/contact.html')

def solo(request):
    return render(request, 'typing_pages/solo.html')

def multiplayer(request):
    return render(request, 'typing_pages/multiplayer.html')

