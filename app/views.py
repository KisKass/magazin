import datetime
from pprint import pprint

from django.db.models import Sum
from django.shortcuts import render, redirect

from app.models import Item, Cart, CartItem, Order


# Create your views here.



def home(request):

    return render(request, 'home.html')


def item(request, id):
    item_obj = Item.objects.get(pk=id)
    context = {
        'item': item_obj,
    }
    if request.POST:
        pprint(request.POST)
        current_user_cart = Cart.objects.get_or_create(user=request.user)
        current_user_cart.items.add(item_obj, through_defaults={'quantity': request.POST['quantity']})
    return render(request, 'item.html', context)


def checkout(request):
    user_cart = Cart.objects.get(user=request.user.pk)
    if request.POST:
        print(request.POST)
        new_order = Order(
            user=request.user,
            phone_number=request.POST['phone'],
            name=request.POST['name'],
            address=request.POST['address'],
            email=request.POST['email'],
            extra_info=request.POST['extra'],
            status='В обработке',
            cart=user_cart,
            date=datetime.date.today()
        )
        new_order.save()
        return redirect('orders')

    user_cart_items = CartItem.objects.filter(cart=user_cart)
    cart_sum = user_cart_items.aggregate(Sum('item__price'))
    print(cart_sum['item__price__sum'])
    context = {'uc': user_cart,
               'uci': user_cart_items,
               'ucs': cart_sum['item__price__sum'],

               }
    return render(request, 'checkout.html', context)


def orders(request):
    context = {
        'orders': Order.objects.filter(user=request.user)
    }
    return render(request, 'orders.html', context)


def order(request, id):
    order_obj = Order.objects.get(pk=id)
    user_cart = order_obj.cart
    user_cart_items = CartItem.objects.filter(cart=user_cart)
    cart_sum = user_cart_items.aggregate(Sum('item__price'))
    print(cart_sum['item__price__sum'])
    context = {'uc': user_cart,
               'uci': user_cart_items,
               'ucs': cart_sum['item__price__sum'],
               'order': order_obj
               }
    return render(request, 'order.html', context)


def profile():
    pass


def catalog(request):
    return render(request, 'item_catalog.html')


def service():
    pass


def cart(request):
    user_cart = Cart.objects.get(user=request.user.pk)
    user_cart_items = CartItem.objects.filter(cart=user_cart)
    cart_sum = user_cart_items.aggregate(Sum('item__price'))
    print(cart_sum['item__price__sum'])
    context = {'uc': user_cart,
               'uci': user_cart_items,
               'ucs': cart_sum['item__price__sum'],

               }
    return render(request, 'cart.html', context)


def login(request):
    if request.POST:
        pprint(request.META['HTTP_REFERER'])
    return redirect(request.META.get('HTTP_REFERER'))


def logout():
    pass
