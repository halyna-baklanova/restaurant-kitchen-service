from http.client import responses

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from management.models import Dish, DishType

DISH_URL = reverse("management:dish-list")

class PublicCookiesTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(DISH_URL)
        self.assertNotEquals(response.status_code, 200)


class PrivateCookiesTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="12345",
        )
        self.client.force_login(self.user)

    def test_retrieve_dishes_list(self):
        dish_type = DishType.objects.create(name="Main")
        Dish.objects.create(name="Bread", description="Bread", price=100, dish_type=dish_type)
        Dish.objects.create(name="Br", description="Bgad", price=20, dish_type=dish_type)
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )

    def test_template_name_dish_type(self):
        DishType.objects.create(name="Smakota")
        url = reverse("management:dish-type-list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "management/dish_type_list.html")
