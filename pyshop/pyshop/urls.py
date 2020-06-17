"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('products/', include('products.urls')),
                  path('', views.index, name='home'),
                  path('about/', views.about, name='about'),
                  path('contact', views.contact_us, name='contact us'),
                  path('terms', views.terms, name='terms'),
                  path('warranty', views.warranty, name='warranty'),
                  path('shipping', views.shipping, name='shipping'),
                  path('refund_return', views.refund_return, name='refund_return'),
                  path('faq', views.faq, name='faq'),
                  path('signin_signup', views.signin_signup, name='signin_signup'),
                  path('privacy', views.privacy, name='privacy'),
                  path('size_chart', views.size_chart, name='size_chart'),
                  path('cart', views.cart, name='cart'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
