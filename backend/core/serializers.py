from rest_framework import serializers
from .models import List, Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['url', 'name', 'done']


class ListSerializer(serializers.HyperlinkedModelSerializer):
    # Notar que foi necessário alterar a ordem em que as classes aparecem no arquivo.
    # A classe ItemSerializer é referenciada na classe ListSerializer, então a classe ItemSerializer
    # deve ser declarada antes da classe ListSerializer. Caso contrário, o código não funcionará. 🤦‍♂️
    item_set = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = List
        # fields = '__all__'
        fields = ['name', 'owner', 'url', 'item_set']