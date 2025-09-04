from django.shortcuts import render

def home(request):
    return render(request,'website/home.html')

def login_view(request):
    pass

def signup_view(request):
    pass