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

        print(serializer)

    def perform_destroy(self, instance):
        instance.image_source.delete_all_created_images()
        instance.image_source.delete(save=False)
        instance.delete()

    def perform_update(self, serializer):
        instance = self.get_object()
        print(instance.image_source)
        instance.image_source.delete_all_created_images()
        instance.image_source.delete(save=False)
        serializer.save()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


