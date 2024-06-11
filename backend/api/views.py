from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Users
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny , IsAuthenticated


# Create your views here.

@api_view(["POST","GET"])
@permission_classes([AllowAny])  
def user_list_create(request):
    if request.method == "GET":
        users = Users.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def user_update_delete(request, id):
    try: 
        user = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response({"error": "User not found with the specified ID"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    