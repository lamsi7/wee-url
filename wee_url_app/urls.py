from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="wee_url-index"),
    path("generate/", views.generate_short_url, name="wee_url-generates"),
    path(
        "<str:query>/",
        views.redirect_from_short_url,
        name="wee_url-redirect",
    ),
]
