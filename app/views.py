from django.shortcuts import render, redirect
from .models import InventoryItem
from .forms import AddItem
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


# Create your views here.

def home(request):

    context = {}

    return render(request, 'app/index.html', context)

@login_required(login_url='login')
def store(request):

    store_items = InventoryItem.objects.all()

    page_title = 'Items in store'

    context = {
        'store_items': store_items,
        'page_title': page_title,
    }

    return render(request, 'app/store.html', context)

@login_required(login_url='login')
def add_item(request):

    if request.method == 'POST':

        form = AddItem(request.POST)

        if form.is_valid():

            form.save()

            return redirect('add_item')

    else:

        form = AddItem()

    page_title = 'Add item to store'

    context = {
        'form': form,
        'page_title': page_title,
    }

    return render(request, 'app/add_item.html', context)

@login_required(login_url='login')
def edit_item(request, slug):

    item_to_edit = InventoryItem.objects.get(slug=slug)

    if request.method == 'POST':

        form = AddItem(request.POST, instance=item_to_edit)

        if form.is_valid():

            form.save()

            return redirect('store')

    else:

        form = AddItem()

    page_title = 'Edit store item'

    context = {
        'form': form,
        'page_title': page_title,
    }

    return render(request, 'app/edit_item.html', context)

@login_required(login_url='login')
def delete_item(request, id):

    item_to_delete = InventoryItem.objects.get(id=id)

    item_to_delete.delete()

    return redirect('store')

@login_required(login_url='login')
def store_item(request, slug):

    item = InventoryItem.objects.filter(slug=slug)

    page_title = 'Store item details'

    context = {
        'item': item,
        'page_title': page_title,
    }

    return render(request, 'app/store_item.html', context)