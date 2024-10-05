from django import forms
from django.contrib.auth.forms import UserCreationForm

from management.models import Cook, DishType, Dish


class CookCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class CookUpdateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )

class DishTypeCreateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class DishTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class DishCreateForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "dish_type",
        ]


class DishUpdateForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "dish_type",
        ]


class DishCookSearchForm(forms.Form):
    cook = forms.CharField(max_length=255, required=False)


