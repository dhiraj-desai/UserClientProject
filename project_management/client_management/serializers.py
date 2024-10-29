from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ProjectSerializerSpecific(serializers.ModelSerializer):
    # users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id", "project_name"]


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id", "project_name", "users"]

    # Overriding the created_by field to return username instead of user instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["created_by"] = instance.created_by.username
        representation["client"] = (
            instance.client.client_name
        )  # Assuming client_name exists in Client model
        return representation


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = [
            "id",
            "client_name",
            "created_at",
            "created_by",
            "updated_at",
            "projects",
        ]


class ClientSerializerSpecific(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = ProjectSerializerSpecific(many=True, read_only=True)

    class Meta:
        model = Client
        fields = [
            "id",
            "client_name",
            "created_at",
            "created_by",
            "updated_at",
            "projects",
        ]
