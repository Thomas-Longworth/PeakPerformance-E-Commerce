from django.shortcuts import render, redirect
from .forms import refundForm
from django.contrib import messages

from .models import Refund

# Create your views here.
# Create your views here.


def request_view(request):
    if request.method == "POST":
        form = refundForm(request.POST)
        form.save()
        messages.success(request, f'Refund request sucessfully submitted')
        return redirect('main')

    form = refundForm()

    context = {
        'form': form,
    }
    return render(request, 'refunds/refund.html', context)


def site_refunds(request):
    return render(request, 'refunds/refund_admin.html')
