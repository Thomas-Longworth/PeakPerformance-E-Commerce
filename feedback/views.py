from django.shortcuts import render, redirect
from .forms import feedbackForm
from .models import UserFeedback

# Create your views here.


def feedback_view(request):
    if request.method == "POST":
        form = feedbackForm(request.POST)
        form.save()
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
