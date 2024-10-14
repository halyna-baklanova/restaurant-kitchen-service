from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.views import generic

from management.models import Dish, Cook, DishType

def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
    }
    return render(request, "management/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "management/dish_type_list.html"

    context_object_name = "dish_types_list"  # Назва контексту

    def get_queryset(self):
        return DishType.objects.prefetch_related("dishes").all()

    def get_success_url(self):
        return reverse("management:dish-type-list")