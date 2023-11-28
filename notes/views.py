from .models import Todonote
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def home(request):
    form = NoteForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                form = NoteForm(request.POST)
                if form.is_valid():
                    note = form.save(commit=False)
                    note.username = request.user
                    note.save()
                    messages.success(
                        request,
                        "Your notes added.",
                        extra_tags="alert alert-success alert-dismissible fade show",
                    )
                    return redirect("notes:view_note", note.id)
                else:
                    messages.error(
                        request,
                        "Oops could not add your note.",
                        extra_tags="alert alert-danger alert-dismissible fade show",
                    )
            except Exception:
                messages.error(
                    request,
                    "Oops some error occured",
                    extra_tags="alert alert-danger alert-dismissible fade show",
                )
                pass
            return redirect("notes:home")
        else:
            messages.error(
                request,
                "Please login to add notes.",
                extra_tags="alert alert-primary alert-dismissible fade show",
            )
            return redirect("accounts:login")
    notes = {}
    if request.user.is_authenticated:
        notes = Todonote.objects.filter(username=request.user)

    return render(request, "notes/home.html", {"notes": notes, "form": form})


def about(request):
    if request.user.is_authenticated:
        messages.success(
            request,
            f"Welcome here,  {request.user.username} !!",
            extra_tags="alert alert-primary alert-dismissible fade show",
        )
    else:
        messages.success(
            request,
            "Please login to manage your notes.",
            extra_tags="alert alert-primary alert-dismissible fade show",
        )

    return render(request, "notes/about.html")


@login_required
def view_note(request, pk):
    notes = {}
    try:
        notes = Todonote.objects.filter(username=request.user, pk=pk)
    except Todonote.DoesNotExist:
        messages.error(
            request,
            "Note does not exist.",
            extra_tags="alert alert-danger alert-dismissible fade show",
        )
        pass
    return render(request, "notes/viewnote.html", {"notes": notes})


@login_required
def edit_note(request, note_id):
    # Retrieve the note based on the note_id or return a 404 if not found
    try:
        note = get_object_or_404(Todonote, username=request.user, pk=note_id)
    except Todonote.DoesNotExist:
        messages.error(
            request,
            "Note does not exist.",
            extra_tags="alert alert-danger alert-dismissible fade show",
        )
        return redirect("notes:home")

    # Check if the user has permission to edit the note (e.g., the note's owner)
    if request.user != note.username:
        return HttpResponseForbidden("You don't have permission to edit this note.")

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            # Optionally, you can return a JSON response indicating success
            messages.success(
                request,
                "Note updated successfully.",
                extra_tags="alert alert-success alert-dismissible fade show",
            )
            # print("Updated note")
            return JsonResponse(
                {"redirect_url": reverse("notes:view_note", args=[note_id])}
            )
            # return redirect("notes:view_note", note_id)
            # return JsonResponse({"message": "Todonote updated successfully"})
        else:
            # If form validation fails, return a JSON response with error details
            errors = form.errors.as_json()
            # messages.error(
            #     request,
            #     "Can't update your note. Please try again.",
            #     extra_tags="alert alert-danger alert-dismissible fade show",
            # )
            return JsonResponse({"errors": errors}, status=400)
    else:
        form = NoteForm(instance=note)

    # Render the HTML template with the form
    # return render(request, 'edit_note.html', {'form': form, 'note': note})
    return redirect("notes:home")


@login_required
def delete_note(request, pk):
    if request.user.is_authenticated:
        try:
            notes = Todonote.objects.filter(username=request.user, pk=pk)
            notes.delete()
            messages.success(
                request,
                "Note deleted",
                extra_tags="alert alert-success alert-dismissible fade show",
            )
        except Todonote.DoesNotExist:
            messages.error(
                request,
                "Note does not exist",
                extra_tags="alert alert-danger alert-dismissible fade show",
            )
            pass
    else:
        messages.error(
            request,
            "Please login to delete your note.",
            extra_tags="alert alert-primary alert-dismissible fade show",
        )
        return redirect("accounts:login")
    return redirect("notes:home")


@login_required
def get_note_data(request, note_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                note = get_object_or_404(Todonote, pk=note_id)
                note_data = {
                    "id": note_id,
                    "title": note.title,
                    "description": note.description,
                }
                # print(note_data)
                return JsonResponse(note_data)
            except Todonote.DoesNotExist:
                return JsonResponse({"error": "Note does not exist."}, status=400)
        else:
            return redirect("notes:home")
    else:
        return redirect("accounts:login")

