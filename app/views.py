from django.shortcuts import render

# Create your views here.
def app(request):
    return render(request,'app/index.html')
def login(request):
    return render(request,'app/login.html')
def sign_up(request):
    return render(request,'app/sign_up.html')