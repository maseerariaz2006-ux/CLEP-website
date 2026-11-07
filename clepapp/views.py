from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def focus(request):
    return render(request, 'core/focus.html')

def teams(request):
    return render(request, 'core/teams.html')

def contact(request):
    return render(request, 'core/contact.html')
