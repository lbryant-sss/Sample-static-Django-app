from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Example: Send an email
            send_mail(
                f'Message from {name}',  # subject
                message,  # message
                email,  # from email
                ['bryige.it@gmail.com'],  # recipient list
            )
            
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
