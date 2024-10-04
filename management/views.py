from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
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


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "management/dish_type_list.html"
    context_object_name = "dish_types_list"
    paginate_by = 5


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "management/dish_type_detail.html"
    context_object_name = "dish_type"


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish
