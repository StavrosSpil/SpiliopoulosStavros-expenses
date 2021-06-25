from django.contrib import admin
from .models import Profile, Expense, Building, Apartment, Payment

# Register your models here.

admin.site.register(Profile)
admin.site.register(Expense)
admin.site.register(Building)
admin.site.register(Apartment)
admin.site.register(Payment)
