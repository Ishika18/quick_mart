from django.contrib import messages
from django.shortcuts import render, redirect
from scanner.scan import scan_code


def home(request):
    return render(request, 'home.html')


def scan(request):
    context = scan_code(request.user.profile)
    print(context)
    if context:
        print(context['unmatched_labels'])
        if context['unmatched_labels'] == set():
            messages.success(request, f'The Product matches your preferences')
        else:
            labels = ''
            for label in context['unmatched_labels']:
                labels += label + ' ,'
            messages.info(request, f'Sorry! This product is not {labels[:-2].replace("_", " ").capitalize()}')
    return redirect(home)
