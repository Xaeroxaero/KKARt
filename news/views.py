from rest_framework import permissions
from products.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from news.serializers import NewSerializer
from news.models import New
from core.settings import os


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'news': reverse('new-list', request=request, format=format)
    })



class NewViewSet(viewsets.ModelViewSet):


    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_destroy(self, instance):
        image_directory = ((os.path.normpath(instance.image_source.path)))
        os.remove(image_directory)
        instance.delete()

