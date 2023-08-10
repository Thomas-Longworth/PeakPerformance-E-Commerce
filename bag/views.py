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
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if request.method == "POST":
        bag.pop(item_id)
        messages.success(
            request, f'Sucessfully removed to your bag')

    request.session['bag'] = bag
    return redirect('view_bag')


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None

        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(
            request, f'Sucessfully removed {product.name} to your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
