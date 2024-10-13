from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Cook(AbstractUser):
    social = models.CharField(null=True, blank=True, max_length=63)
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["username"]
        permissions = [
            ("can_edit_cook", "Can edit cook"),
            ("can_delete_cook", "Can delete cook"),
            ("can_create_cook", "Can create cook"),
        ]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("management:cook-detail", kwargs={"pk": self.pk})


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("management:dish-type-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes",
        blank=True,
        null=True,
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="dishes"
    )

    class Meta:
        verbose_name_plural = "dishes"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("management:dish-detail", kwargs={"pk": self.pk})
