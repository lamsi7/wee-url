from django.shortcuts import render, HttpResponse
from .models import UrlModel
import uuid

# Create your views here.


def index(request):
    return render(request, "wee_url_app/index.html")


def generate_short_url(request):
    if request.method == "POST":
        link = request.POST["link"]
        gen_id = str(uuid.uuid4())[:5]
        new_url = UrlModel(link=link, gen_id=gen_id)
        new_url.save()
