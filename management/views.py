from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse, reverse_lazy
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        return context


class CookDetailView(generic.DetailView):
    model = Cook


class CookCreateView(generic.CreateView):
    model = Cook


class CookUpdateView(generic.UpdateView):
    model = Cook


class CookDeleteView(
    generic.DeleteView
):
    model = Cook

    def get_success_url(self):
        return reverse("management:cook-list")


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 5
    context_object_name = "dish_types_list"
    template_name = "management/dish_type_list.html"


    def get_queryset(self):
        return DishType.objects.prefetch_related("dishes").all()

    def get_success_url(self):
        return reverse("management:dish-type-list")


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "management/dish_type_form.html"


class DishTypeCreateView(generic.CreateView):
    model = DishType
    template_name = "management/dish_type_form.html"


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    template_name = "management/dish_type_form.html"


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    template_name = "management/dish_type_confirm_delete.html"

    def get_success_url(self):
        return reverse("management:dish-type-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 4


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = Dish


class DishUpdateView(generic.UpdateView):
    model = Dish
    template_name = "management/dish_form.html"

    def get_success_url(self):
        return reverse_lazy("management:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish

    def get_success_url(self):
        return reverse("management:dish-list")