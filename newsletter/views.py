# app_name/views.py

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
from .models import EmailSubscriber


def email_form_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Save the email address to the database
            subscriber = EmailSubscriber(email=email)
            subscriber.save()

            # Send the email
            send_mail(
                'Subject of the email',
                'Content of the email',
                'your_gmail_username@gmail.com',
                [email],
                fail_silently=False,
            )
            return render(request, 'main/index.html')
    else:
        form = EmailForm()
    return render(request, 'newsletter/email_form.html', {'form': form})
