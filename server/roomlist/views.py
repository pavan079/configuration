from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer
from rest_framework.generics import ListCreateAPIView


class RoomListCreateView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# GET and POST methods to retrieve and create rooms
@api_view(['GET', 'POST'])
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()  # Fetch all rooms
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)  # Return room data as JSON

    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)  # Parse incoming data
        if serializer.is_valid():
            serializer.save()  # Save new room to DB
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT, and DELETE methods for a specific room (by ID)
@api_view(['GET', 'PUT', 'DELETE'])
def room_detail(request, room_id):
    try:
        room = Room.objects.get(id=room_id)  # Get room by ID
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)  # Return room data

    elif request.method == 'PUT':
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update room details in DB
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        room.delete()  # Delete room from DB
        return Response(status=status.HTTP_204_NO_CONTENT)
