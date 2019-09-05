from django.shortcuts import render
from products.models import Product

# Create your views here.
def category(request, category_id):
    products = Product.objects.filter(category__id=category_id)
    #print(products.values('category__name')[0]['category__name'])
    context = {
        'products': products,
        'category_name':products.values('category__name')[0]['category__name'],
    }

    return render(request, 'products/products.html', context)







