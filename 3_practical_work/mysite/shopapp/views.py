from django.shortcuts import render
from .models import Product, Order

def shop_index(request):
    return render(request, 'shopapp/index.html')

def products_list(request):
    products = Product.objects.all()
    return render(request, 'shopapp/products.html', {'products': products})

def orders_list(request):
    # Используйте select_related и prefetch_related для оптимизации запросов
    orders = Order.objects.select_related('user').prefetch_related('products').all()
    return render(request, 'shopapp/orders.html', {'orders': orders})
