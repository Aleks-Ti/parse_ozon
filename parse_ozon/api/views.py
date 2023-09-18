from rest_framework import status, viewsets, mixins

from api.serializers import ProductSerializer
from product.models import Product


class ProductView(
    mixins.CreateModelMixin,  # POST
    mixins.ListModelMixin,  # GET
    mixins.RetrieveModelMixin,  # GET detail
    viewsets.GenericAPIView
):
    queryset = Product.objects.all()  # Замените YourProductModel на вашу модель товара
    serializer_class = ProductSerializer  # Замените YourProductSerializer на ваш сериализатор товара

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
