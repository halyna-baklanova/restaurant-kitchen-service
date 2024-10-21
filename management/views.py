from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from management.forms import (
    CookCreationForm,
    CookSearchForm,
    DishTypeSearchForm,
    DishCookSearchForm, DishCookForm,

)
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

def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", status=403)

class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.CreateView
):
    model = Cook
    form_class = CookCreationForm

    def test_func(self):
        return self.request.user.is_staff


class CookUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView
):
    model = Cook
    fields = [
        "username",
        "first_name",
        "last_name",
        "social",
        "years_of_experience",
    ]
    success_url = reverse_lazy("management:cook-list")
    template_name = "management/cook_form.html"

    def test_func(self):
        return self.request.user.is_staff



class CookDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView
):
    model = Cook
    def get_success_url(self):
        return reverse("management:cook-list")

    def test_func(self):
        return self.request.user.is_staff


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5
    context_object_name = "dish_types_list"
    template_name = "management/dish_type_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishTypeDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    model = DishType


class DishTypeCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("management:dish-type-list")
    template_name = "management/dish_type_form.html"


class DishTypeUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView
):
    model = DishType
    template_name = "management/dish_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("management:dish-type-list")

    def test_func(self):
        return self.request.user.is_staff


class DishTypeDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView
):
    model = DishType
    template_name = "management/dish_type_confirm_delete.html"
    success_url = reverse_lazy("management:dish-type-list")

    def test_func(self):
        return self.request.user.is_staff


class DishListView(
    LoginRequiredMixin,
    generic.ListView
):
    model = Dish
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        cook = self.request.GET.get("cook", "")
        context["search_form"] = DishCookSearchForm(initial={"cook": cook})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        cook_name = self.request.GET.get("cook")
        if cook_name:
            queryset = queryset.filter(
                Q(cooks__first_name__icontains=cook_name) |
                Q(cooks__last_name__icontains=cook_name)
            ).distinct()
        return queryset

class DishDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    model = Dish


class DishCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Dish
    success_url = reverse_lazy("management:dish-list")
    template_name = "management/dish_form.html"
    fields = "__all__"


class DishUpdateView(
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Dish
    template_name = "management/dish_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("management:dish-list")


class DishAssignCooksView(
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Dish
    form_class = DishCookForm


class DishDeleteView(
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Dish

    def get_success_url(self):
        return reverse("management:dish-list")