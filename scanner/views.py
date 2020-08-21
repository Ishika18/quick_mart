from django.shortcuts import render, redirect
from scanner.scan import scan_code


# Create your views here.
def home(request):
    return render(request, 'home.html')


def scan(request):
    scan_code(request.user.profile)
    return redirect(home)
