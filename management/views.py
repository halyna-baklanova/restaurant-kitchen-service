from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from wheel.cli.convert import convert

from management.models import Dish, Cook


def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
    }
    return render(request, "management/index.html", context=context)