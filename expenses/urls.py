"""expenses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from buildings import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('admin/', admin.site.urls),
    path('apartments/', views.apartments, name='apartments'),
    path('building/<str:pk>/', views.building, name='building'),
    path('user/<str:pk>/', views.user, name='user'),
    path('administrator_page/', views.administratorPage, name='administrator_page'),
    path('tenant_page/', views.tenantPage, name='tenant_page'),
    path('calculate_expenses/', views.calculateExpenses, name='calculate_expenses'),
    path('expense/<str:pk>/', views.expense, name='expense'),
    path('tenant_expenses/', views.tenantExpenses, name='tenant_expenses'),
    path('payments/', views.payments, name='payments'),
    path('view_payments/<str:pk>/', views.viewPayment, name='view_payments'),
    path('consumption/', views.Consum, name='consumption'),


    path('profile_settings<str:pk>/', views.updateProfile, name='update_profile'),

    path('create_expense/<str:pk>/', views.createExpense, name='create_expense'),
    path('delete_expense/<str:pk>/', views.deleteExpense, name='delete_expense'),

    path('create_user/', views.createUser, name='create_user'),
    path('update_user/<str:pk>/', views.updateUser, name='update_user'),
    path('delete_user/<str:pk>/', views.deleteUser, name='delete_user'),

    path('create_building/', views.createBuilding, name='create_building'),
    path('update_building/<str:pk>/', views.updateBuilding, name='update_building'),
    path('delete_building/<str:pk>/', views.deleteBuilding, name='delete_building'),

    path('create_apartment/', views.createApartment, name='create_apartment'),
    path('update_apartment/<str:pk>/', views.updateApartment, name='update_apartment'),
    path('delete_apartment/<str:pk>/', views.deleteApartment, name='delete_apartment'),

]
