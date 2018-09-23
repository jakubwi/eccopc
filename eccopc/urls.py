from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('produkty/', views.CategoryPageView.as_view(), name='products'),
    path('produkty/<category_name_slug>/', views.ProductListView, name='product_list'),
    path('produkty/<category_name_slug>/<slug:slug>/', views.ProductDetailView, name='product_detail'),
    path('wsparcie-techniczne/', views.search, name='search_sn'),
    path('wsparcie-techniczne/<pk>/', views.SerialNumberDetailView.as_view(), name='serialnumber_detail'),
    
]