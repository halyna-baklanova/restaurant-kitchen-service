from django.test import TestCase

from management.models import Cook, DishType


class ModelTests(TestCase):
    def test_cook_str(self):
        cook = Cook.objects.create(
            username="aaaaa",
            first_name="Cook",
            last_name="Last_Cook",
        )
        self.assertEqual(str(cook), f"{cook.username} ({cook.first_name} {cook.last_name})")

    def test_dish_type_str(self):
        dishtype = DishType.objects.create(name="name123")
        self.assertEqual(str(dishtype), dishtype.name)

    def test_create_cook_with_years_of_experience(self):
        cook = Cook.objects.create(
            username="aaaaa",
            years_of_experience=2000,
        )
        self.assertEqual(cook.years_of_experience, 2000)

