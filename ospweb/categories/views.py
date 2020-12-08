from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets

from . import models, serializers


# Create your views here.
class ListCreateCategory(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class RetrieveUpdateDestroyCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ListCreateProduct(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return self.queryset.filter(category_id=self.kwargs.get("category_pk"))

    def perform_create(self, serializer):
        category = get_object_or_404(models.Category, pk=self.kwargs.get("category_pk"))
        serializer.save(category=category)


class RetrieveUpdateDestroyProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            category_id=self.kwargs.get("category_pk"),
            pk=self.kwargs.get("pk"),
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
