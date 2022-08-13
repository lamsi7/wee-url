from django import forms
from .models import UrlModel


class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlModel
        fields = ["link"]
        labels = {"link": ""}
        widgets = {
            "link": forms.TextInput(
                attrs={"id": "inputURL", "placeholder": "Paste URL here"}
            )
        }
