from django import forms

from .models import Todonote


class NoteForm(forms.ModelForm):
    class Meta:
        model = Todonote
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control my-2", "placeholder": "Enter note title"},
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control my-2",
                    "rows": "3",
                    "placeholder": "Enter note description",
                },
            ),
        }
