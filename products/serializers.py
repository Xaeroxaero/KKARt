from django.contrib.auth.models import User
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image_source = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'filters__water__url'),
            ('thumbnail', 'thumbnail__800x800')
        ]
    )

    class Meta:
        model = Product
        fields = ('url', 'id', 'owner',
                  'title', 'metod', 'image_source', 'price', 'painting_size', 'about')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'products')
