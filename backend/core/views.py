from rest_framework import permissions, viewsets

from .serializers import ListSerializer, ItemSerializer

from .models import List, Item

# Create your views here.
class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Lists to be viewed or edited.
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
