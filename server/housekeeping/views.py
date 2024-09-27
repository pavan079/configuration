from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Housekeeper
from .serializers import HousekeeperSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Housekeeping API!")


# Handle GET and POST requests
@api_view(['GET', 'POST'])
def housekeeper_list(request):
    if request.method == 'GET':
        housekeepers = Housekeeper.objects.all()
        serializer = HousekeeperSerializer(housekeepers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HousekeeperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handle DELETE requests (you should add this method as well)
@api_view(['DELETE'])
def housekeeper_delete(request, pk):
    try:
        housekeeper = Housekeeper.objects.get(pk=pk)
    except Housekeeper.DoesNotExist:
        return Response({"error": "Housekeeper not found"}, status=status.HTTP_404_NOT_FOUND)
    
    housekeeper.delete()
    return Response({"message": "Housekeeper deleted successfully"}, status=status.HTTP_204_NO_CONTENT)