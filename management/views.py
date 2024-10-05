from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic


from management.models import Dish, Cook, DishType


from management.forms import (
    CookCreateForm,
    CookUpdateForm,
    DishTypeCreateForm,
    DishTypeUpdateForm,
)


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
    }
    return render(request, "management/index.html", context=context)


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreateForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    form_class = CookCreateForm


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "management/dish_type_list.html"
    context_object_name = "dish_types_list"
    paginate_by = 5


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "management/dish_type_detail.html"
    context_object_name = "dish_type"


class DishTypeCreateView(generic.CreateView):
    model = DishType
    form_class = DishTypeCreateForm
    template_name = "management/dish_type_form.html"


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    form_class = DishTypeUpdateForm
    template_name = "management/dish_type_form.html"


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    form_class = DishTypeCreateForm
    template_name = "management/dish_type_confirm_delete.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
