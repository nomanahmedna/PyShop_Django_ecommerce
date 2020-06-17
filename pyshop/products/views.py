import a as a
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil


def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))

    allProducts = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(product_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProducts.append([prod,range(1,nSlides),nSlides])

    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # allProducts = [[products,range(1,nSlides),nSlides],
    #                [products,range(1,nSlides),nSlides],]
    params = {'allProducts': allProducts}
    return render(request, 'index.html', params)


def new(request):
    return HttpResponse("This is New Products Page")


def trending(request):
    return HttpResponse("This is Trending Products Page")


def product_view(request):
    return HttpResponse("This is products view Page")


def check_out(request):
    return HttpResponse("This is check out Page")


def search(request):
    return HttpResponse("This is search Page")


def tracking(request):
    return HttpResponse("This is tracking Page")
