
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Products

class ProductsListView(ListView):
    model = Products
    template_name = "products/products_list.html"
    context_object_name = "products"

class ProductsCreateView(CreateView):
    model = Products
    fields = ["name", "price", "category"]
    success_url = reverse_lazy("products_list")

class ProductsUpdateView(UpdateView):
    model = Products
    fields = ["name", "price", "category"]
    success_url = reverse_lazy("products_list")

class ProductsDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy("products_list")