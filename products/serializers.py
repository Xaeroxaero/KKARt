from rest_framework import serializers
from products.models import Product
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .filters import WatermarkImage


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
