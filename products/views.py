from django.shortcuts import render, get_object_or_404
from products.choices import status_choices, price_choices, category_choices

# Create your views here.
from products.models import Product


def index(request):
    return render(request, 'products/products.html')

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/product.html', context)

def search(request):
    queryset_list = Product.objects.order_by('-create_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            queryset_list = queryset_list.filter(status__iexact=status)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    if 'categories' in request.GET:
        categories = request.GET['categories']
        if categories:
            queryset_list = queryset_list.filter(category__name__iexact=categories)

    context = {
        'products': queryset_list,
        'status_choices': status_choices,
        'price_choices': price_choices,
        'category_choices': category_choices,
        'values': request.GET,
    }
    return render(request, 'products/search.html', context)

