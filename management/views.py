from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q


from management.models import Dish, Cook, DishType


from management.forms import (
    CookCreateForm,
    CookUpdateForm,
    DishTypeCreateForm,
    DishTypeUpdateForm,
    DishCreateForm,
    DishUpdateForm,
    DishCookSearchForm
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


class CookListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Cook
    paginate_by = 5

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return self.render_to_response({"error": "You do not have permission to view this page."})


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook

    def get(self, request, pk):
        cook = get_object_or_404(Cook, pk=pk)
        return render(request, "management/cook_detail.html", {"cook": cook})

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

    def get_queryset(self):
        queryset = super().get_queryset()
        cook_name = self.request.GET.get("cook")
        if cook_name:
            queryset = queryset.filter(
                Q(cooks__first_name__icontains=cook_name) | Q(cooks__last_name__icontains=cook_name)
            ).distinct()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        cook = self.request.GET.get("cook", "")
        context["search_form"] = DishCookSearchForm(initial={"cook": cook})
        return context


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishCreateForm


class DishUpdateView(generic.UpdateView):
    model = Dish
    form_class = DishUpdateForm


class DishDeleteView(generic.DeleteView):
    model = Dish
    form_class = DishCreateForm
    success_url = reverse_lazy("management:dish-list")


class AssignCookView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request, dish_id):
        dish = Dish.objects.get(id=dish_id)
        cooks = Cook.objects.all()
        return render(request, "management/assign_cook.html", {"dish": dish, "cooks": cooks})

    def post(self, request, dish_id):
        dish = Dish.objects.get(id=dish_id)
        cook_id = request.POST.get("cook")
        cook = Cook.objects.get(id=cook_id)

        dish.cooks.add(cook)
        return redirect("management:dish-detail", pk=dish_id)
