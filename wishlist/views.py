from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Wishlist
from .forms import WishForm
# Create your views here.

def index(request):
    wish_list = Wishlist.objects.order_by('id')

    form = WishForm()

    context = {'wish_list' : wish_list, 'form' : form}

    return render(request, 'wishlist/index.html', context)

@require_POST
def addWish(request):
    form = WishForm(request.POST)

    print(request.POST['text'])
    if form.is_valid():
        new_wish = Wishlist(text=request.POST['text'])
        new_wish.save()

    return redirect('index')

def completeWish(request, wish_id):
    wish_list = Wishlist.objects.get(pk=wish_id)
    wish_list.complete = True
    wish_list.save()

    return redirect('index')

def deleteCompleted(request):
    Wishlist.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Wishlist.objects.all().delete()

    return redirect('index')
