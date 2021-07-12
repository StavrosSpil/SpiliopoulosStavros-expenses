from django.http import HttpResponse
from django.shortcuts import redirect


# view func einai ayth pou xrhsimopoioume ekeinh thn stigmh
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# gives access to a specific role in a page
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')

        return wrapper_func

    return decorator


# gives access only to the site-admin
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Administrators':
            return redirect('administrator_page')

        if group == 'Tenants':
            return redirect('tenant_page')

        if group == 'Site-admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
