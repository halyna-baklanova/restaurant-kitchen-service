from django.urls import path, include

from management.views import (
    index,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishTypeListView,
    DishTypeDetailView,
    DishListView,
    DishDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
path(
        "cooks/create",
        CookCreateView.as_view(),
        name="cook-create"
    ),
path(
        "cooks/update/<int:pk>",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
path(
        "cooks/delete/<int:pk>",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/<int:pk>", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
]

app_name = "management"
