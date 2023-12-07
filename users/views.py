from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View

from users.models import User


# login view
class LoginPageView(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'error': 'Invalid login'})

    def form_valid(self, form):
        response = super().form_valid(form)

        return response

    def get_success_url(self):
        return reverse_lazy('accounts')


# sign up view
class SignupView(View):
    def post(self, request):
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_number = request.POST.get('number')
        user_address = request.POST.get('address')

        User.objects.create_user(username=user_name, email=user_email,
                                 password=user_password, phone_number=user_number,
                                 address=user_address)

        return redirect('login')

    def get(self, request):
        return render(request, 'signup.html')
