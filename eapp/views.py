from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product


# Create your views here.
def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, "eapp/index.html", context)


def add_item(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    description = request.POST.get('description')
    image = request.FILES.get('upload')
    if image is not None:
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
        return render(request, "eapp/additem.html")
    else:
        return render(request, 'eapp/additem.html', )


def indexItem(request, id):
    item = Product.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, "eapp/detail.html", context)


def update_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.description = request.POST.get('description')
        item.image = request.FILES.get('upload', item.image)
        item.save()
        return redirect("/eapp/")
    context = {'item': item}
    return render(request, 'eapp/updateitem.html', context)


def delete_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("/eapp/")
    context = {'item': item}
    return render(request, 'eapp/deleteitem.html', context)
