from rest_framework import permissions
from products.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from contact.serializers import ContactSerializer
from contact.models import Contact
from core.settings import os
from django.core.mail import send_mail

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'contact': reverse('contact-list', request=request, format=format)
    })



class ContactViewSet(viewsets.ModelViewSet):


    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        new = self.get_object()
        return Response(new.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        print(send_mail('Subject here', 'Here is the message.', 'from@example.com',
                  ['to@example.com'], fail_silently=False))

    def perform_destroy(self, instance):
        instance.delete()