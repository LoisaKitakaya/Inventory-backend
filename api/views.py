from rest_framework import generics
from .serializers import InventorySerializer
from app.models import InventoryItem

# Create your views here.
class InventoryList(generics.ListAPIView):

    queryset = InventoryItem.objects.all()

    serializer_class = InventorySerializer

class InventoryListDetail(generics.RetrieveAPIView):

    queryset = InventoryItem.objects.all()

    serializer_class = InventorySerializer