from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import JsonResponse


def HomeView(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validate form data
        if fullname and contact and email and message:
            # Save to the database
            data = Contact(full_name=fullname, number=contact, email=email, message=message)
            data.save()

            # Handle AJAX requests
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Message Sent!'})
            else:
                messages.success(request, 'Message Sent!')
        else:
            # Handle errors for both regular POST and AJAX requests
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Please fill in all fields.'})
            else:
                messages.error(request, 'Please fill in all fields.')

    # Render the form page

    return render(request, 'index.html')

def AboutView(request):
    return render(request, 'about.html')

def serviceView(request):
    return render(request, 'service.html')

def ContactView(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validate form data
        if fullname and contact and email and message:
            # Save to the database
            data = Contact(full_name=fullname, number=contact, email=email, message=message)
            data.save()

            # Handle AJAX requests
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Message Sent!'})
            else:
                messages.success(request, 'Message Sent!')
        else:
            # Handle errors for both regular POST and AJAX requests
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Please fill in all fields.'})
            else:
                messages.error(request, 'Please fill in all fields.')

    # Render the form page
    return render(request, 'contact.html')

def BlogView(request):
    return render(request, 'blog.html')