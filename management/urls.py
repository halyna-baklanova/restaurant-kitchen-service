

from django.urls import path, include

from management.views import index

urlpatterns = [
    path("", index, name="index"),
]
