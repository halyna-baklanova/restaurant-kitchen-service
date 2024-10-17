from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from management.models import Dish, Cook, DishType

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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        return context


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook


class CookDeleteView(
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Cook

    def get_success_url(self):
        return reverse("management:cook-list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5
    context_object_name = "dish_types_list"
    template_name = "management/dish_type_list.html"


    def get_queryset(self):
        return DishType.objects.prefetch_related("dishes").all()

    def get_success_url(self):
        return reverse("management:dish-type-list")


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "management/dish_type_form.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    template_name = "management/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    template_name = "management/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "management/dish_type_confirm_delete.html"

    def get_success_url(self):
        return reverse("management:dish-type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 4


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    template_name = "management/dish_form.html"

    def get_success_url(self):
        return reverse_lazy("management:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish

    def get_success_url(self):
        return reverse("management:dish-list")