from django.urls import path

from management.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    CookDetailView,
    DishTypeDetailView,
    DishDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/",
         CookListView.as_view(),
         name="cook-list"
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
        "dish-types/<int:pk>",
        DishTypeDetailView.as_view(),
        name="dish-types-detail"
    ),
    path(
        "dishes/", DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "dishes/<int:pk>",
        DishDetailView.as_view(),
        name="dish-detail"
    )
]

app_name = "management"
