from django import forms
from django.contrib.auth.forms import UserCreationForm

from management.models import Cook, DishType


class CookCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )

    # def clean(self):
    #     validate_years_of_experience(self.cleaned_data)

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
