from rest_framework import serializers
from contact.models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ('id', 'email', 'subject', 'body')