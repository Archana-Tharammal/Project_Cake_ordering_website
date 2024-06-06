
from django.shortcuts import render, redirect

from .models import product
from .forms import CartForm


def home(request):
    return render(request, 'home.html')


def index(request):
    produ = {
        'pro': product.objects.all()
    }
    return render(request, 'index.html', produ)
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data.get('product_id')
            return redirect('cart', product_id=product_id)




    return render(request, 'index.html', {'products': produ['pro'], 'form': form})



def cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_image_url = request.POST.get('product_image_url')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        return render(request, 'cart.html', {'product_name': product_name, 'product_image_url': product_image_url,'price':price, 'quantity':quantity})
    else:
        return render(request, 'cart.html')


def description(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_image_url = request.POST.get('product_image_url')

        description = request.POST.get('description')
        return render(request, 'description.html',{'product_name': product_name, 'product_image_url': product_image_url,'description':description})
    else:
        return render(request, 'description.html')

def about(request):
    return render(request, 'about.html')
def details(request):
    return render(request, 'details.html')
def success(request):
    return render(request, 'success.html')
