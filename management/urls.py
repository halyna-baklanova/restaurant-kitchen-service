from django.urls import path

from management.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    CookDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/",
         CookListView.as_view(),
         name="cooks"
         ),
path(
        "cooks/<int:pk>",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dishes/", DishListView.as_view(),
        name="dish-list"
    ),
]

app_name = "management"
