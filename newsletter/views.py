from django.shortcuts import render, redirect

from django.contrib import messages



# Views here.
def subscription(request):
 
    return render(request, "newsletter/subscribe.html")
