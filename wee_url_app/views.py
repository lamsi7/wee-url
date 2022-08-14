from django.shortcuts import redirect, render, HttpResponse
from .forms import UrlForm
from .models import UrlModel
import uuid
from django.http import HttpResponseBadRequest, JsonResponse


def index(request):
    if request.method == "GET":
        form = UrlForm()
        return render(request, "wee_url_app/index.html", {"form": form})


def generate_uuid():
    _id = str(uuid.uuid4())[:5]
    # Check if _id already exists in the table
    exists = UrlModel.objects.filter(gen_id=_id).exists()
    while exists:
        print("Generating new id")
        _id = str(uuid.uuid4())[:5]
        exists = UrlModel.objects.filter(gen_id=_id).exists()
    return _id


def generate_short_url(request):
    if request.method == "POST":
        print(f"hereeeeeeee: {request.POST}")
        link = request.POST["link"]
        filled_form = UrlForm({"link": link})
        if filled_form.is_valid():
            new_url = filled_form.save(commit=False)
            gen_id = generate_uuid()
            new_url.gen_id = gen_id
            new_url.save()
            # Get host so we can join it with gen_id and display it
            host = request.get_host()
            response = {"link": link, "gen_id": gen_id, "host": host}
            print(response)
            return JsonResponse(response)


def redirect_from_short_url(request, query):
    if len(query) != 5:
        return HttpResponseBadRequest("Incorrect length of the query ")
    obj = UrlModel.objects.filter(gen_id=query)
    if obj.exists():
        return redirect(obj.values()[0]["link"])
    return HttpResponseBadRequest("URL does not exist in the database")
