from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InventorySerializer
from app.models import InventoryItem

# Create your views here.
class InventoryList(generics.ListAPIView):

    queryset = InventoryItem.objects.all()

    serializer_class = InventorySerializer

class InventoryListDetail(generics.RetrieveAPIView):

    queryset = InventoryItem.objects.all()

    serializer_class = InventorySerializer

@api_view(['GET'])
def inventory_list(request, format=None):

    if request.method == 'GET':

        items = InventoryItem.objects.all()

        serializer = InventorySerializer(items, many=True)

        return Response(serializer.data)

@api_view(['GET'])
def inventory_item_detail(request, pk, format=None):
    
    try:

        item = InventoryItem.objects.get(pk=pk)

    except InventoryItem.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = InventorySerializer(item)

        return Response(serializer.data)