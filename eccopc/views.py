from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models
from .models import Category, Product

class HomePageView(TemplateView):
    template_name = 'home.html'

class CategoryPageView(ListView):
    model = models.Category
    template_name = 'categories.html'

def ProductListView(request, category_name_slug):
    context_dict = {}
   
    try: 
        category = Category.objects.get(slug=category_name_slug)
        products = Product.objects.filter(category=category)
        context_dict['products'] = products
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['products'] = None
        context_dict['category'] = None

    return render(request, 'product_list.html', {'products': products, 'category': category, })

def ProductDetailView(request, category_name_slug, slug):
    context_dict = {}
    product = Product.objects.get(slug=slug)
   
    try: 
        category = Category.objects.get(slug=category_name_slug)
        product = Product.objects.get(slug=slug)
        context_dict['product'] = product

    except Product.DoesNotExist:
        context_dict['product'] = None


    return render(request, 'product_detail.html', {'product': product, 'category': category, })