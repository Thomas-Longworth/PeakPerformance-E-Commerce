from django.shortcuts import render, redirect
from .forms import feedbackForm

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
