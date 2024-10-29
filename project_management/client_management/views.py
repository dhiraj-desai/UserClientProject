from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, ClientSerializerSpecific
from django.contrib.auth.models import User


# List all clients or create a new client
@api_view(["GET", "POST"])
@permission_classes([])
def client_list_create(request):
    if request.method == "GET":
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, or delete a client
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([])
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == "GET":
        serializer = ClientSerializerSpecific(client)
        return Response(serializer.data)
    elif request.method in ["PUT", "PATCH"]:
        serializer = ClientSerializerSpecific(
            client, data=request.data, partial=(request.method == "PATCH")
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create a new project for a client and assign users
@api_view(["POST"])
@permission_classes([])
def create_project_for_client(request, client_id):
    # Retrieve the client by ID
    client = get_object_or_404(Client, pk=client_id)

    # Get the project name from the request data
    project_name = request.data.get("project_name")

    # Retrieve user IDs from the request data
    user_ids = [user["id"] for user in request.data.get("users", [])]

    # Get users with the specified IDs
    users = User.objects.filter(id__in=user_ids)

    # Create the project instance
    project = Project.objects.create(
        project_name=project_name, client=client, created_by=request.user
    )

    # Assign users to the project
    project.users.set(users)
    project.save()

    # Serialize the project instance and return the response
    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# List all projects assigned to the logged-in user
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_assigned_projects(request):
    projects = request.user.assigned_projects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


# Create your views here.
