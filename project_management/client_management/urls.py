from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.client_list_create, name="client-list-create"),
    path("clients/<int:pk>/", views.client_detail, name="client-detail"),
    path(
        "clients/<int:client_id>/projects/",
        views.create_project_for_client,
        name="create-project-for-client",
    ),
    path("projects/", views.user_assigned_projects, name="user-assigned-projects"),
]
