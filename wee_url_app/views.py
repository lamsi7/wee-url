from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "wee_url_app/index.html")
