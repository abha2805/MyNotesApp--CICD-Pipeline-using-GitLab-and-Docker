from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("viewnote/<int:pk>", views.view_note, name="view_note"),
    path("editnote/<int:note_id>/", views.edit_note, name="edit_note"),
    path("deletenote/<int:pk>", views.delete_note, name="delete_note"),
    path("api/notes/<int:note_id>/", views.get_note_data, name="get_note_data"),
    # path("api/notes/<int:pk>/", views.api_notes, name="api_notes"),
]
