from rest_framework import serializers
from products.models import Product
from django.contrib.auth.models import User
from products.models import New

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='product-highlight', format='html')

    class Meta:
        model = Product
        fields = ('url', 'id', 'highlight', 'owner',
                  'title','metod', 'image_source', 'price',)



class UserSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'products')

class NewSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = New
        fields = ('owner', 'url', 'id', 'title', 'news')
