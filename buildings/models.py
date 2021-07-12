from django.contrib.auth.models import User
from django.db import models


class TypeRoles(models.TextChoices):
    ADMINISTRATOR = 'ADMINISTRATOR'
    TENANT = 'TENANT'
    SITE_ADMIN = 'SITE_ADMIN'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    cellphone = models.PositiveIntegerField(null=True)
    role = models.CharField(max_length=13, choices=TypeRoles.choices)

    def __str__(self):
        return self.user.username


class Building(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200, null=True)
    floors = models.PositiveSmallIntegerField(null=True)
    apartments = models.PositiveSmallIntegerField(null=True)
    reserve = models.FloatField(null=True)

    def __str__(self):
        return self.address


class Apartment(models.Model):
    building = models.ForeignKey(Building, null=True, on_delete=models.SET_NULL)
    tenant = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    floor = models.PositiveSmallIntegerField(null=True)
    square_meters = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    owner = models.BooleanField(default=False)
    heating = models.FloatField(null=True)
    elevator = models.FloatField(null=True)
    general_expenses = models.FloatField(null=True)
    fi = models.FloatField(null=True)

    def __str__(self):
        return f"{self.building.address} - {self.tenant}"


class TypeExpenses(models.TextChoices):
    HEATING = 'HEATING'
    ELEVATOR = 'ELEVATOR'
    GENERAL = 'GENERAL'


class Expense(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    total = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    document = models.CharField(max_length=200, null=True)
    type_expenses = models.CharField(max_length=10, choices=TypeExpenses.choices, default=TypeExpenses.GENERAL)
    month = models.PositiveSmallIntegerField(null=True)
    year = models.PositiveSmallIntegerField(null=True)


class Payment(models.Model):
    apartment = models.ForeignKey(Apartment, null=True, on_delete=models.SET_NULL)
    month = models.PositiveSmallIntegerField(null=True)
    year = models.PositiveSmallIntegerField(null=True)
    total_heating = models.FloatField(null=True)
    total_elevator = models.FloatField(null=True)
    total_general = models.FloatField(null=True)
    payment_made = models.BooleanField(default=False)


class Consumption(models.Model):
    apartment = models.ForeignKey(Apartment, null=True, on_delete=models.SET_NULL)
    month = models.PositiveSmallIntegerField(null=True)
    year = models.PositiveSmallIntegerField(null=True)
    consumption = models.PositiveIntegerField(null=True)

