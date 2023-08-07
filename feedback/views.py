from django.shortcuts import render, redirect
from .forms import feedbackForm
from .models import UserFeedback
from django.contrib import messages

# Create your views here.


def feedback_view(request):
    if request.method == "POST":
        form = feedbackForm(request.POST)
        form.save()
        messages.success(request, f'Thanks for your feedback!')
        return redirect('main')

    form = feedbackForm()

    context = {
        'form': form,
    }

    return render(request, 'feedback/feedback.html', context)


def site_feedback(request):
    feed = UserFeedback.objects.all()
    context = {
        'feed': feed
    }

    return render(request, 'feedback/site_feedback.html', context)
