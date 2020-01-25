from django.shortcuts import render, redirect, reverse


# Create your views here.
def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    try:
        quantity = int(request.POST.get('quantity'))
    except:
        return redirect(reverse('index'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjust the quantity of the specified product by the specified amount"""
    try:
        quantity = int(request.POST.get('quantity'))
    except:
        return redirect(reverse('view_cart'))
    
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
