from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "category", "description", "created_at")
        model = models.Product


class CategorySerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, read_only=True)
    products = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="api:product-detail"
    )

    class Meta:
        fields = ("id", "name", "products", "created_at")
        model = models.Category
