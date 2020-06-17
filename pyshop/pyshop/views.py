from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def about(request):
    return render(request, '/products/about.html')


def contact_us(request):
    return HttpResponse("this is contact us page")


def terms(request):
    return HttpResponse("this is terms & Condition page")


def warranty(request):
    return HttpResponse("this is warranty page")


def shipping(request):
    return HttpResponse("this is shipping page")


def refund_return(request):
    return HttpResponse("this is refund and return page")


def faq(request):
    return HttpResponse("this is FAQ page")


def signin_signup(request):
    return HttpResponse("this is user sign in and sign up page")


def privacy(request):
    return HttpResponse("this is privacy policy page")


def size_chart(request):
    return HttpResponse("this is size chart")


def search(request):
    return HttpResponse("this is search page")


def cart(request):
    return HttpResponse("this is cart page")