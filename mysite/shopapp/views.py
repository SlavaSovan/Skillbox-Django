from django.http import (HttpResponse,
                         HttpRequest)
from timeit import default_timer
from django.shortcuts import render


def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 74990),
        ('Desktop', 138990),
        ('Smartphone', 39990)
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, 'shopapp/shop-index.html',
                  context=context)
