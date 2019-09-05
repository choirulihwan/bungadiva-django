from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from products.choices import status_choices, price_choices, category_choices
from categories.models import Category


def index(request):
    #return HttpResponse('<h1>Bismillah</h1>')
    products = Product.objects.order_by('-create_date').filter(status=Product.READY, is_published=True)[:3]

    context = {
        'products': products,
        'status_choices' : status_choices,
        'price_choices': price_choices,
        'category_choices': category_choices,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
