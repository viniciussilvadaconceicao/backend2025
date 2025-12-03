from django.urls import path
from products.views import ProductsListView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("create/", ProductsCreateView.as_view(), name="products_create"),
    path("edit/<int:pk>/", ProductsUpdateView.as_view(), name="products_update"),
    path("delete/<int:pk>/", ProductsDeleteView.as_view(), name="products_delete"),
]