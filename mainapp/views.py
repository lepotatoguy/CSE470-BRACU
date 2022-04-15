from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.views.generic.list import ListView  # listing
from django.views.generic.detail import DetailView  # detail viewing
# creating, updating/modify
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# redirecting to another link after certain task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin


class Login(LoginView):
    template_name = 'mainapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class Index(LoginRequiredMixin, ListView):
    model = Finance  # database
    context_object_name = 'transactions'  # context object inside the html
    template_name = 'mainapp/index.html'  # specifying template name


class TransactionDetail(DetailView):
    model = Finance
    context_object_name = 'transaction'
    template_name = 'mainapp/transaction_detail.html'


class TransactionCreate(CreateView):
    model = Finance
    # fields = ['status', 'remarks'] #fixed fields
    fields = '__all__'  # all fields
    success_url = reverse_lazy('index')  # redirect after successful creation
    context_object_name = 'transaction_create'
    template_name = 'mainapp/transaction_form.html'


class TransactionUpdate(UpdateView):
    model = Finance
    fields = '__all__'  # all fields
    success_url = reverse_lazy('index')  # redirect after successful creation
    template_name = 'mainapp/transaction_form.html'


class TransactionDelete(DeleteView):
    model = Finance
    context_object_name = 'transaction'
    success_url = reverse_lazy('index')  # redirect after successful creation
    # template_name = 'mainapp/transaction_form.html'

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def index(request):
#     user_list = User.objects.all()
#     paramters = {'user_list': user_list, }
#     return render(request, 'index.html', paramters)
#     # return HttpResponse(output)
