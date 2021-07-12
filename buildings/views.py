from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import CreateUserForm, BuildingForm, ApartmentForm, ProfileForm, ExpenseForm, PaymentForm, ConsumptionForm
from .filters import ApartmentFilter, ExpenseFilter, PaymentFilter

from django.contrib.auth.decorators import login_required

from .models import Building, Profile, Apartment, Expense, Payment, Consumption

from django.shortcuts import get_object_or_404

from datetime import datetime


@login_required(login_url='login')
@admin_only
def home(request):
    profiles = Profile.objects.all()
    buildings = Building.objects.all()

    context = {'buildings': buildings, 'profiles': profiles}

    return render(request, 'buildings/dashboard.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'buildings/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'buildings/register.html', context)


@login_required(login_url='login')
@admin_only
def apartments(request):
    apartments = Apartment.objects.all()

    myFilter = ApartmentFilter(request.GET, queryset=apartments)
    apartments = myFilter.qs

    context = {'apartments': apartments, 'myFilter': myFilter}
    return render(request, 'buildings/apartments.html', context)


@login_required(login_url='login')
@admin_only
def building(request, pk):
    building = Building.objects.get(id=pk)

    context = {'building': building}
    return render(request, 'buildings/building.html', context)


@login_required(login_url='login')
@admin_only
def user(request, pk):
    profile = Profile.objects.get(id=pk)
    apartment = get_object_or_404(Apartment, tenant=profile)

    context = {'profile': profile, 'apartment': apartment}
    return render(request, 'buildings/user.html', context)


@login_required(login_url='login')
@admin_only
def createBuilding(request):
    form = BuildingForm()

    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'buildings/building_form.html', context)


@login_required(login_url='login')
@admin_only
def updateBuilding(request, pk):
    building = Building.objects.get(id=pk)
    form = BuildingForm(instance=building)

    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'buildings/building_form.html', context)


@login_required(login_url='login')
@admin_only
def deleteBuilding(request, pk):
    building = Building.objects.get(id=pk)
    if request.method == 'POST':
        building.delete()
        return redirect('home')

    context = {'building': building}
    return render(request, 'buildings/delete_building.html', context)


@login_required(login_url='login')
@admin_only
def createUser(request):
    form = CreateUserForm()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'buildings/user_form.html', context)


@login_required(login_url='login')
@admin_only
def updateUser(request, pk):
    profile = Profile.objects.get(id=pk)
    form = CreateUserForm(instance=profile.user)

    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=profile.user)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'buildings/user_form.html', context)


@login_required(login_url='login')
@admin_only
def deleteUser(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile.delete()
        profile.user.delete()
        return redirect('home')

    context = {'profile': profile}
    return render(request, 'buildings/delete_user.html', context)


@login_required(login_url='login')
@admin_only
def createApartment(request):
    form = ApartmentForm()

    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apartments')

    context = {'form': form}
    return render(request, 'buildings/apartment_form.html', context)


@login_required(login_url='login')
@admin_only
def updateApartment(request, pk):
    apartment = Apartment.objects.get(id=pk)
    form = ApartmentForm(instance=apartment)

    if request.method == 'POST':
        form = ApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            return redirect('apartments')

    context = {'form': form}
    return render(request, 'buildings/apartment_form.html', context)


@login_required(login_url='login')
@admin_only
def deleteApartment(request, pk):
    apartment = Apartment.objects.get(id=pk)
    if request.method == 'POST':
        apartment.delete()
        return redirect('apartments')

    context = {'apartment': apartment}
    return render(request, 'buildings/delete_apartment.html', context)


@login_required(login_url='login')
@admin_only
def updateProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'buildings/profile_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrators', 'Tenants'])
def tenantPage(request):
    user = request.user
    profile = user.profile
    apartment = get_object_or_404(Apartment, tenant=profile)

    context = {'apartment': apartment, 'profile': profile}
    return render(request, 'buildings/tenant_page.html', context)


@login_required(login_url='login')
# only administrators have access to this page
@allowed_users(allowed_roles=['Administrators'])
def administratorPage(request):
    user = request.user
    profile = user.profile
    building = get_object_or_404(Building, profile=profile)
    apartments = Apartment.objects.filter(building=building)

    context = {'building': building, 'apartments': apartments}
    return render(request, 'buildings/administrator_page.html', context)


@login_required(login_url='login')
def calculateExpenses(request):
    total_heating = 0.0
    total_elevator = 0.0
    total_general = 0.0
    total_product = 0.0
    apartment_heating = {}
    apartment_elevator = {}
    apartment_general = {}
    consumption = {}
    product = {}
    division = {}
    apartment_cons = {}

    # get the current month and year
    current_month = datetime.now().month
    current_year = datetime.now().year

    user = request.user
    profile = user.profile
    building = get_object_or_404(Building, profile=profile)
    expenses = Expense.objects.filter(profile=building.profile)
    current_expenses = Expense.objects.filter(month=current_month).filter(year=current_year)
    apartments = Apartment.objects.filter(building=building)

    # calculate the total of every type of expense
    for expense in current_expenses:
        if expense.type_expenses == 'HEATING':
            total_heating = total_heating + expense.total
        elif expense.type_expenses == 'ELEVATOR':
            total_elevator = total_elevator + expense.total
        else:
            total_general = total_general + expense.total

    # get the consumption for every apartment
    for apartment in apartments:
        consumption[apartment.id] = Consumption.objects.filter(apartment=apartment)[0]

    # multiplies heating millimetre with the hours of every apartment
    # and gets the total of those multiplication
    for apartment in apartments:
        product[apartment.id] = apartment.heating * consumption[apartment.id].consumption
        total_product = total_product + product[apartment.id]

    # divides each product with the total_product
    for apartment in apartments:
        division[apartment.id] = product[apartment.id] / total_product

    # get the product of fi and millimetres of every apartment
    for apartment in apartments:
        product_static = apartment.heating * apartment.fi

    static = 1 - product_static

    # multiplies the division of every apartment with the static and adds the product_static
    for apartment in apartments:
        apartment_cons[apartment.id] = product_static + division[apartment.id] * static

    # total heating equals to the total petroleum that the building bought for this month
    for apartment in apartments:
        apartment_heating[apartment.id] = total_heating * apartment_cons[apartment.id]
        apartment_elevator[apartment.id] = total_elevator * apartment.elevator
        apartment_general[apartment.id] = total_general * apartment.general_expenses
        payment = Payment(apartment=apartment, month=current_month, year=current_year,
                          total_heating=apartment_heating[apartment.id],
                          total_elevator=apartment_elevator[apartment.id],
                          total_general=apartment_general[apartment.id])
        # checks if a specific payment exists and if it does it deletes it to replace it with the new one
        if Payment.objects.filter(apartment=apartment, month=current_month, year=current_year).exists():
            Payment.objects.filter(apartment=apartment, month=current_month, year=current_year).delete()

        payment.save()

    context = {'building': building, 'expenses': expenses, 'apartments': apartments,
               'total_heating': total_heating, 'total_elevator': total_elevator,
               'total_general': total_general, 'apartment_heating': apartment_heating,
               'apartment_elevator': apartment_elevator, 'apartment_general': apartment_general,
               'payment': payment}
    return render(request, 'buildings/calculate_expenses.html', context)


@login_required(login_url='login')
def expense(request, pk):
    building = Building.objects.get(id=pk)
    expenses = Expense.objects.filter(profile=building.profile)
    # apartments = Apartment.objects.filter(building=building)

    myFilter = ExpenseFilter(request.GET, queryset=expenses)
    expenses = myFilter.qs

    context = {'building': building, 'expenses': expenses, 'myFilter': myFilter}
    return render(request, 'buildings/expense.html', context)


@login_required(login_url='login')
def createExpense(request, pk):
    user = request.user
    profile = user.profile
    building = Building.objects.get(id=pk)

    # initialize profile
    form = ExpenseForm(initial={'profile': profile})
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Expense()
            obj.profile = profile
            obj.total = form.cleaned_data['total']
            obj.month = form.cleaned_data['month']
            obj.year = form.cleaned_data['year']
            obj.document = form.cleaned_data['document']
            obj.type_expenses = form.cleaned_data['type_expenses']
            obj.save()
            handle_uploaded_file(request.FILES['document'], obj.document, obj.id)
            obj.document = str(obj.id) + str(obj.document)
            obj.save()
            return redirect('administrator_page')

    context = {'form': form, 'building': building, 'profile': profile}
    return render(request, 'buildings/expense_form.html', context)


# a method to handle uploaded files
def handle_uploaded_file(f, path, pk):
    with open('static/documents/' + str(pk) + str(path), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required(login_url='login')
def deleteExpense(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('administrator_page')

    context = {'expense': expense}
    return render(request, 'buildings/delete_expense.html', context)


@login_required(login_url='login')
def tenantExpenses(request):
    user = request.user
    profile = user.profile
    apartment = Apartment.objects.get(tenant=profile)
    payments = Payment.objects.filter(apartment=apartment)

    myFilter = PaymentFilter(request.GET, queryset=payments)
    payments = myFilter.qs

    context = {'payments': payments, 'myFilter': myFilter}
    return render(request, 'buildings/tenant_expenses.html', context)


@login_required(login_url='login')
def payments(request):
    payments = {}
    total = {}
    user = request.user
    profile = user.profile
    building = Building.objects.get(profile=profile)
    apartments = Apartment.objects.filter(building=building)
    for apartment in apartments:
        payments[apartment.id] = Payment.objects.filter(apartment=apartment)[0]
        total[apartment.id] = payments[apartment.id].total_heating + payments[apartment.id].total_elevator + payments[
            apartment.id].total_general

    context = {'payments': payments, 'apartments': apartments, 'building': building, 'total': total}
    return render(request, 'buildings/payments.html', context)


@login_required(login_url='login')
def viewPayment(request, pk):
    payment = Payment.objects.get(id=pk)
    total = payment.total_heating + payment.total_elevator + payment.total_general

    form = PaymentForm(instance=payment)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('administrator_page')

    context = {'payment': payment, 'form': form, 'total': total}
    return render(request, 'buildings/view_payments.html', context)


@login_required(login_url='login')
def Consum(request):
    user = request.user
    profile = user.profile
    building = Building.objects.get(profile=profile)
    apartments = Apartment.objects.filter(building=building)

    #form = ConsumptionForm(apartments=apartments)
    form = ConsumptionForm()

    if request.method == 'POST':
        #form = ConsumptionForm(request.POST, apartments=apartments)
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrator_page')

    context = {'building': building, 'apartments': apartments, 'form': form}
    return render(request, 'buildings/consumption_form.html', context)
