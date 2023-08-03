# newsletter/views.py
from django.shortcuts import render, redirect
from .forms import SubscriberForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage, get_connection


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            send_newsletter_email(
                form.cleaned_data['name'], form.cleaned_data['email'])
            # Create a 'success' URL for successful form submission
            return redirect('subscribe')
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})


def send_newsletter_email(name, email):
    subject = 'Welcome to our newsletter!'
    message = f'Hi {name},\n\nThank you for subscribing to our newsletter!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
