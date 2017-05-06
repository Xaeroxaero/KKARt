from rest_framework import serializers

from news.models import New


class NewSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = New
        fields = ('owner', 'url', 'id', 'title', 'news', 'image_source', 'created')
