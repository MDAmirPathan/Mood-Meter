# from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from products.models.customer import Customer
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        pasword = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(pasword, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                request.session['f'] = customer.first_name
                print(email, customer.id)
                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!!'
        else:
            error_message = 'Email or Password invalid !!!'
        # print(customer)
        # print(email)
        return render(request, 'login.html', {'error': error_message})
