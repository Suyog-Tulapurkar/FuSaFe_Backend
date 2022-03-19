from rest_framework import serializers
from .models import Treeviewlist

class TreeviewlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Treeviewlist
        fields = ('id', 'part_id', 'part_name', 'section_id', 'section_name', 'workproduct')