from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Building, Apartment, Profile, TypeExpenses, Payment, Consumption


class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'cellphone', 'role']


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_made']


class ConsumptionForm(ModelForm):
    class Meta:
        model = Consumption
        fields = '__all__'


# class ConsumptionForm(ModelForm):
# class Meta:
# model = Consumption
# fields = ['month', 'year', 'consumption']

# def __init__(self, building, *args, **kwargs):
# super(ConsumptionForm, self).__init__(*args, **kwargs)
# self.fields['apartment'].queryset = Apartment.objects.filter(building=building)


class ExpenseForm(forms.Form):
    profile = forms.CharField(max_length=100)
    document = forms.FileField()
    total = forms.FloatField()
    month = forms.IntegerField()
    year = forms.IntegerField()
    type_expenses = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))

    # apartment = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        # self.fields['apartment'].choices = [(apartment.id, apartment.tenant) for apartment in apartments]
        self.fields['type_expenses'].choices = TypeExpenses.choices
        self.fields['profile'].widget.attrs['readonly'] = True
