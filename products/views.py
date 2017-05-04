from products.models import Product
from products.serializers import ProductSerializer
from products.serializers import UserSerializer
from rest_framework import permissions
from products.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from django.contrib.auth.models import User
from core.settings import os
from products.models import Product


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
    })


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def perform_destroy(self, instance):

        image_directory = ((os.path.normpath(instance.image_source.path)))
        os.remove(image_directory)
        instance.image_source.delete_sized_images()
        instance.delete()

    def perform_update(self, serializer):
        queryset = Product.objects.all()
        print(queryset)
        instance = serializer.save()
        print(instance.image_source)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
