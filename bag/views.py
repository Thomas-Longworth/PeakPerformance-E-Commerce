from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product


def view_bag(request):

    return render(request, 'bag.html')


def add_to_bag(request, item_id):

    product = Product.objects.get(pk=item_id)
   

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {product.name} to your bag')
    else:
        bag[item_id] = quantity
      

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
