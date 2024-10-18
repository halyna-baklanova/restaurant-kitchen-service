from django import forms
from django.contrib.auth.forms import UserCreationForm

from management.models import Cook, DishType, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "social",
            "years_of_experience",
        )

#
# class CookUpdateForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Cook
#         fields = UserCreationForm.Meta.fields + (
#             "first_name",
#             "last_name",
#             "social",
#             "years_of_experience",
#         )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
        "placeholder": "Search by cook"
        }
        )
    )


# class DishTypeCreateForm(forms.ModelForm):
#     class Meta:
#         model = DishType
#         fields = ["name"]


# class DishTypeUpdateForm(forms.ModelForm):
#     class Meta:
#         model = DishType
#         fields = ["name"]


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
        "placeholder": "Search by dish type"
        }
        )
    )


# class DishCreateForm(forms.ModelForm):
#     class Meta:
#         model = Dish
#         fields = [
#             "name",
#             "description",
#             "price",
#             "dish_type",
#             "cooks"
#         ]


# class DishUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Dish
#         fields = [
#             "name",
#             "description",
#             "price",
#             "dish_type",
#             "cooks"
#         ]

class DishCookUpdateForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Dish
        fields = ["cooks"]


class DishCookSearchForm(forms.Form):
    cook = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
        "placeholder": "Search by cook"
        }
        )
    )

# class DishForm(forms.ModelForm):
#     cooks = forms.ModelMultipleChoiceField(
#         queryset=Cook.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
#     class Meta:
#         model = Dish
#         fields = "__all__"
