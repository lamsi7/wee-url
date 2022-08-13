from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="wee_url-index"),
    path("generate/", views.generate_short_url, name="wee_url-generates"),
]
