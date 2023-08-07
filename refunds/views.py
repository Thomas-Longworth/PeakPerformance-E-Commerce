from django.shortcuts import render

# Create your views here.


def request_view(request):
    return render(request, 'refunds/refund.html')
