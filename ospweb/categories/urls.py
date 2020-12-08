from django.urls import path

from . import views

app_name = "category"

urlpatterns = [
    path("", views.ListCreateCategory.as_view(), name="category_list"),
    path(
        "<pk>/", views.RetrieveUpdateDestroyCategory.as_view(), name="category_detail"
    ),
    path(
        "<category_pk>/products/",
        views.ListCreateProduct.as_view(),
        name="product_list",
    ),
    path(
        "<category_pk>/products/<pk>/",
        views.RetrieveUpdateDestroyProduct.as_view(),
        name="product_detail",
    ),
]
