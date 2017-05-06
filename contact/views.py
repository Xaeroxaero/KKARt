from django.core.mail import send_mail
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from contact.models import Contact
from contact.serializers import ContactSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'contact': reverse('contact-list', request=request, format=format)
    })


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        new = self.get_object()
        return Response(new.highlighted)

    def perform_create(self, serializer):
        print(serializer.data['email'])

        send_mail(serializer.data['subject'], serializer.data['body'], serializer.data['email'],
                  ['tomasz.budzyn91@gmail.com'], fail_silently=False)

    def perform_destroy(self, instance):
        instance.delete()
