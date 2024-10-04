from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    social = models.CharField(null=True, blank=True, max_length=63)
    years_of_experience = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return (f"{self.username} "
                f"{self.first_name} {self.last_name}")


class DishType(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ("name",)
        verbose_name = "Dish Type"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dish_type")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cooks")

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Dishes"


    def __str__(self):
        return f"{self.name}. Price: {self.price} {self.dish_type.name}"

    def get_absolute_url(self):
        return reverse("management:dish_detail", kwargs=[str(self.id)])
