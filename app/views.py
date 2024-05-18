from pprint import pprint

from django.shortcuts import render

from app.models import Item, Cart


# Create your views here.
def home(request):
    return render(request,'home.html')

def item(request,id):
    item_obj = Item.objects.get(pk=id)
    context = {
        'item':item_obj,
    }
    if request.POST:
        pprint(request.POST)
        current_user_cart = Cart.objects.get(user=request.user)
        current_user_cart.items.add(item_obj,through_defaults={'quantity':request.POST['quantity']})
    return render(request,'item.html',context)

def checkout(request):
    return render()


def profile():
    pass


def catalog(request):
    return render(request,'item_catalog.html')


def service():
    pass


def login():
    pass


def logout():
    pass
