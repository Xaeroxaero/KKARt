from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'products')
