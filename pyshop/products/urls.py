from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products_home'),
    path('new', views.new, name='new'),
    path('trending', views.trending, name='trending'),
    path('product_view', views.product_view, name='product_view'),
    path('check_out', views.check_out, name='check_out'),
    path('search', views.search, name='search'),
    path('tracking', views.tracking, name='tracking'),
]