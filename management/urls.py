from django.urls import path

from management.views import index

app_name = "management"

urlpatterns = [
    path("", index, name="index"),
]
