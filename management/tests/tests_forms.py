from django.test import TestCase
from management.forms import CookCreateForm


class FormTests(TestCase):
    def test_cook_creation_form_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "Test last",
        }
        form = CookCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get("username"), form_data["username"])
        self.assertEqual(form.cleaned_data.get("first_name"), form_data["first_name"])
        self.assertEqual(form.cleaned_data.get("last_name"), form_data["last_name"])
        self.assertTrue(form.cleaned_data.get("password1"))

