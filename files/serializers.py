from rest_framework import serializers
from files.models import File
from django.contrib.auth.models import User

class FileSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='file-highlight', format='html')

    class Meta:
        model = File
        fields = ('url', 'id', 'highlight', 'owner',
                  'title','metod', 'image_source', 'price')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    files = serializers.HyperlinkedRelatedField(many=True, view_name='file-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'files')

